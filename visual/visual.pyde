from cube import Cube
from face import faces
from itertools import cycle

add_library('peasycam')

def process_moves(cube, raw_moves):
    moves = raw_moves.split()
    face_mapper = {
        'U': faces['UP'],
        'D': faces['DOWN'],
        'L': faces['LEFT'],
        'R': faces['RIGHT'],
        'F': faces['FRONT'],
        'B': faces['BACK'],
    }
    for move in moves:
        move += ' '
        face = face_mapper.get(move[0])
        if not face:
            continue

        clockwise = True
        if move[1] == "'":
            clockwise = False
        cube.rotate_face(face, clockwise)
        if move[1] == "2":
            cube.rotate_face(face, clockwise)

def file_selected(selection):
    global moves_iterator, file_name
    if selection is not None:
        file_name = selection.getAbsolutePath()
        with open(selection.getAbsolutePath(), 'r') as file:
            moves_iterator = cycle([line for line in file if line.strip()])
            

def setup():
    frameRate(60)
    size(800, 600, P3D)

    global pg
    pg = createGraphics(width, height, P3D)

    global moves_iterator, file_name
    moves_iterator = cycle(' ')
    file_name = None

    global cube
    cube = Cube()

    cam = PeasyCam(this, pg, 800)
    cam.setRotations(-QUARTER_PI / 3, PI - QUARTER_PI / 3, QUARTER_PI / 15)
    cam.setMinimumDistance(400)
    cam.setMaximumDistance(1200)
    cam.setDistance(cam.getDistance() + 1, 1)
    cam.setDistance(cam.getDistance() - 1, 1)

    selectInput("Select a file with shuffle:", "file_selected")

    font = loadFont("Monospaced.vlw")
    textFont(font)

def draw():
    pg.beginDraw()
    pg.background(55)
    # pg.background(255, 246, 212)

    pg.scale(100)
    pg.rectMode(CENTER)
    cube.show(pg)

    pg.endDraw()
    image(pg, 0, 0)

    textMode(MODEL)
    fill(222, 222, 222)

    textAlign(RIGHT, BOTTOM)
    text_size = height / 40
    textSize(text_size)
    template = "{key:>14} -> {label:<25}"
    text(template.format(key="[N] or [SPACE]", label="apply next line of moves"), width, height - 3 * text_size)
    text(template.format(key="[O]", label="open a new file"), width, height - 2 * text_size)
    text(template.format(key="[R]", label="reset"), width, height - text_size)
    text(template.format(key="[ESC]", label="exit"), width, height)

    global file_name
    if file_name:
        textAlign(RIGHT, TOP)
        text("Showing: {file_name}  ".format(file_name=file_name), width, 0)

def keyPressed():
    global moves_iterator, cube
    if key in (' ', 'n'):
        line = next(moves_iterator)
        process_moves(cube, line)
    elif key == 'o':
        selectInput("Select a file with shuffle:", "file_selected")
    elif key == 'r':
        cube = Cube()
