#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on April 27, 2023, at 19:27
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
score = 0
rounds = 1


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Serotonin-test1'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\91628\\OneDrive - IIT Kanpur\\Desktop\\Replication\\Serotonin-test1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Instructions" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='dl.beatsnoop.com-final-4sLrpV8NGn.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()
sound_1 = sound.Sound('bgm.wav', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
Instructions_Main = visual.TextStim(win=win, name='Instructions_Main',
    text='Greetings, Explorer!\n\nWe warmly welcome you to Egypt. While participating in the treasure hunt, you will encounter a puzzle that involves choosing symbols to discover hidden treasures. However, be aware that certain symbols may cause your gold to diminish due to curses.\n\nTo maximize your gold, observe and learn from the trial rounds to understand the correlation between symbols and their effects on gold and curses.\n\nWe wish you the best of luck!',
    font='Times Newr',
    pos=[0,-0.2], height=0.025, wrapWidth=None, ori=0.0, 
    color=[1.0000, 0.6863, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
continu = visual.TextStim(win=win, name='continu',
    text='Press spacebar to continue',
    font='Open Sans',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
# Run 'Begin Experiment' code from code_5
import csv

part = expInfo['participant']
name = str(part) + ".csv" 

output_file = open(name, "w")

writer = csv.writer(output_file)
Header = ["case","image1", "probability1", "image2", "probability2", "user_choice", "score"]

writer.writerow(Header)


# --- Initialize components for Routine "Instructions_2" ---
sound_2 = sound.Sound('entry.wav', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='dl.beatsnoop.com-final-hNQOS7C1XA.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()
Instructions_Main_2 = visual.TextStim(win=win, name='Instructions_Main_2',
    text='You have now entered a mirrored reality where you can attempt the puzzle 16 times. Each attempt will provide an opportunity for you to learn from the outcomes, but none of these outcomes will have any impact on your actual reality in terms of gold or curses',
    font='Times Newr',
    pos=[0,-0.2], height=0.035, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
continu_2 = visual.TextStim(win=win, name='continu_2',
    text='Press spacebar to continue',
    font='Open Sans',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Instructions_3" ---
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='dl.beatsnoop.com-final-hNQOS7C1XA.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()
Instructions_Main_3 = visual.TextStim(win=win, name='Instructions_Main_3',
    text='Use left and right arrows to select the desired symbol',
    font='Times Newr',
    pos=[0,-0.2], height=0.035, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
continu_3 = visual.TextStim(win=win, name='continu_3',
    text='Press spacebar to continue',
    font='Open Sans',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "trial_4" ---
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from code_6
import random

pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]

times = [0, 0, 0, 0]
number = 0

previous_case = 0
present_case = 0

loop = 0

order = []

image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "trial_2" ---
# Run 'Begin Experiment' code from code_2
arrow_x = 0
arrow_y = 0
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "trial_3" ---
# Run 'Begin Experiment' code from code_3
cases = ["cr", "pr", "cp", "pp"]

gold = "gold.png"
zero = "void.png"
curse = "curse.png"
null = "null.png"

curr_sound = "null.wav"

img_arr = [gold, zero, curse]

score = 0

error_msg = ""




image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sound_3 = sound.Sound('A', secs=1.5, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_29 = visual.ImageStim(
    win=win,
    name='image_29', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "reset_2" ---

# --- Initialize components for Routine "main_instructions" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='dl.beatsnoop.com-final-hNQOS7C1XA.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()
Instructions_Main_4 = visual.TextStim(win=win, name='Instructions_Main_4',
    text='Welcome to the main reality of our game. Your goal is to solve the puzzle and collect as much gold as possible while avoiding curses that may reduce your gold. You will have a limited number of attempts to complete the puzzle, so use them wisely.\n\nAs you progress, you will encounter same symbols that were in mirror dimension that may have similar effects on your gold and curses. Take note of these effects and learn from your previous attempts to increase your chances of success.\n\nRemember that your gold and curses in this reality are real and will impact your overall score. So, be cautious and strategic in your approach to maximize your rewards.\n\nGood luck, and have fun!',
    font='Times Newr',
    pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
continu_4 = visual.TextStim(win=win, name='continu_4',
    text='Press spacebar to continue',
    font='Open Sans',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
sound_7 = sound.Sound('reality.wav', secs=-1, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)

# --- Initialize components for Routine "Rounds" ---
sound_6 = sound.Sound('rounds.wav', secs=-1, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1.0)
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='dl.beatsnoop.com-final-hNQOS7C1XA.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_7 = keyboard.Keyboard()
Instructions_Main_7 = visual.TextStim(win=win, name='Instructions_Main_7',
    text='',
    font='Times Newr',
    pos=[0,-0.2], height=0.035, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
continu_6 = visual.TextStim(win=win, name='continu_6',
    text='Press spacebar to continue',
    font='Open Sans',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "trial_4" ---
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from code_6
import random

pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]

times = [0, 0, 0, 0]
number = 0

previous_case = 0
present_case = 0

loop = 0

order = []

image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "trial_2" ---
# Run 'Begin Experiment' code from code_2
arrow_x = 0
arrow_y = 0
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "trial_3" ---
# Run 'Begin Experiment' code from code_3
cases = ["cr", "pr", "cp", "pp"]

gold = "gold.png"
zero = "void.png"
curse = "curse.png"
null = "null.png"

curr_sound = "null.wav"

img_arr = [gold, zero, curse]

score = 0

error_msg = ""




image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sound_3 = sound.Sound('A', secs=1.5, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_29 = visual.ImageStim(
    win=win,
    name='image_29', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "End_Screen" ---
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='dl.beatsnoop.com-final-4sLrpV8NGn.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()
sound_4 = sound.Sound('post.wav', secs=-1, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)
Instructions_Main_5 = visual.TextStim(win=win, name='Instructions_Main_5',
    text='Congratulations on making it this far in the game! We hope you\'re having a great time so far. As you know, the symbols in the game can have different effects on your gold and curses. In order to better understand your values associated with these symbols, we would like to ask you to play one more quick round.\n\nDon\'t worry, you won\'t lose any gold or suffer any curses in this round. Instead, we simply want to gather some data on the values of the symbols. This will help us analyze your values associated with the symbols\n\nAs an added incentive, we\'d like to share a short story with you. Legend has it that there\'s a hidden treasure deep in the heart of the desert, guarded by a mysterious Sphinx. The Sphinx has the power to grant wealth and prosperity to anyone who can solve its riddles and decipher its secrets. By playing this quick round and helping us gather data, you\'ll be one step closer to unlocking the treasure and achieving true riches.\n\nTo play the quick round, simply follow these instructions:\n\nSelect the "Space Bar" optionx\n.\nChoose the symbols you think will yield the most gold.\n\nOnce you\'ve completed the quick round, we\'ll display your score from the main game. So, what are you waiting for? Take a shot at solving the Sphinx\'s riddles and unlocking the treasure of the desert!\n',
    font='Times Newr',
    pos=[0,0], height=0.025, wrapWidth=None, ori=0.0, 
    color=[0.9608, 0.9608, 0.6471], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
continu_5 = visual.TextStim(win=win, name='continu_5',
    text='Press spacebar to continue',
    font='Open Sans',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "trial_7" ---
image_31 = visual.ImageStim(
    win=win,
    name='image_31', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from code_10
import random

repeated_array = []
array_element = []
for i in range(0, 8):
    for j in range(i + 1, 8):
        array_element.append((i, j))

for i in range(4):
    for element in array_element:
        repeated_array.append(element)

post_learn = repeated_array

times = [0, 0, 0, 0]
number = 0


loop = 0


image_32 = visual.ImageStim(
    win=win,
    name='image_32', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_33 = visual.ImageStim(
    win=win,
    name='image_33', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "trial_6" ---
# Run 'Begin Experiment' code from code_8
arrow_x = 0
arrow_y = 0
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_27 = visual.ImageStim(
    win=win,
    name='image_27', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_28 = visual.ImageStim(
    win=win,
    name='image_28', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "error" ---
# Run 'Begin Experiment' code from code_11
cases = ["cr", "pr", "cp", "pp"]

gold = "gold.png"
zero = "void.png"
curse = "curse.png"
null = "null.png"

img_arr = [gold, zero, curse]

score = 0

error_msg = ""




image_30 = visual.ImageStim(
    win=win,
    name='image_30', 
    image='IMG_0436.jpeg.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_34 = visual.ImageStim(
    win=win,
    name='image_34', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "Final_Score_and_Good_Bye" ---
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='dl.beatsnoop.com-final-4sLrpV8NGn.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()
sound_5 = sound.Sound('end.wav', secs=-1, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1.0)
Instructions_Main_6 = visual.TextStim(win=win, name='Instructions_Main_6',
    text='',
    font='Times Newr',
    pos=[0,-0.2], height=0.025, wrapWidth=None, ori=0.0, 
    color=[1.0000, 0.6863, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
sound_1.setSound('bgm.wav', secs=60, hamming=True)
sound_1.setVolume(1.0, log=False)
# keep track of which components have finished
InstructionsComponents = [image, key_resp, sound_1, Instructions_Main, continu]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image.started')
        image.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play(when=win)  # sync with win flip
    if sound_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_1.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            sound_1.tStop = t  # not accounting for scr refresh
            sound_1.frameNStop = frameN  # exact frame index
            sound_1.stop()
    
    # *Instructions_Main* updates
    if Instructions_Main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Main.frameNStart = frameN  # exact frame index
        Instructions_Main.tStart = t  # local t and not account for scr refresh
        Instructions_Main.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Main, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_Main.started')
        Instructions_Main.setAutoDraw(True)
    
    # *continu* updates
    if continu.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        continu.frameNStart = frameN  # exact frame index
        continu.tStart = t  # local t and not account for scr refresh
        continu.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continu, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continu.started')
        continu.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
sound_1.stop()  # ensure sound has stopped at end of routine
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
sound_2.setSound('entry.wav', hamming=True)
sound_2.setVolume(1.0, log=False)
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Instructions_2Components = [sound_2, image_2, key_resp_2, Instructions_Main_2, continu_2]
for thisComponent in Instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_2
    if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_2.frameNStart = frameN  # exact frame index
        sound_2.tStart = t  # local t and not account for scr refresh
        sound_2.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sound_2.started', tThisFlipGlobal)
        sound_2.play(when=win)  # sync with win flip
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_2.started')
        image_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Instructions_Main_2* updates
    if Instructions_Main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Main_2.frameNStart = frameN  # exact frame index
        Instructions_Main_2.tStart = t  # local t and not account for scr refresh
        Instructions_Main_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Main_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_Main_2.started')
        Instructions_Main_2.setAutoDraw(True)
    
    # *continu_2* updates
    if continu_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        continu_2.frameNStart = frameN  # exact frame index
        continu_2.tStart = t  # local t and not account for scr refresh
        continu_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continu_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continu_2.started')
        continu_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_2" ---
for thisComponent in Instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_2.stop()  # ensure sound has stopped at end of routine
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instructions_3Components = [image_3, key_resp_3, Instructions_Main_3, continu_3]
for thisComponent in Instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3.started')
        image_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Instructions_Main_3* updates
    if Instructions_Main_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Main_3.frameNStart = frameN  # exact frame index
        Instructions_Main_3.tStart = t  # local t and not account for scr refresh
        Instructions_Main_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Main_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_Main_3.started')
        Instructions_Main_3.setAutoDraw(True)
    
    # *continu_3* updates
    if continu_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        continu_3.frameNStart = frameN  # exact frame index
        continu_3.tStart = t  # local t and not account for scr refresh
        continu_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continu_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continu_3.started')
        continu_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_3" ---
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=16.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    import random
    from psychopy.hardware import keyboard
    
    
    if number%4 == 0:
        order = []
        while len(order) < 4:
            temp = random.randint(0, 3)
            if temp not in order:
                order.append(temp)
    
    number += 1
    present_case = order[number%4]
    
    maybe = random.randint(0, 50)
    
    if(maybe%3):
        image1 = pairs[present_case][0]
        image2 = pairs[present_case][1]
    else:
        image1 = pairs[present_case][1]
        image2 = pairs[present_case][0]
    
    img1 = image1
    img2 = image2
    
    image1 = str(image1) + ".png"
    image2 =  str(image2) + ".png"
    
    selected = keyboard.Keyboard(bufferSize=1)
    selected.clearEvents(eventType='keyboard')
    
    loop += 1
    #print(keys[0].name)
    
    
    
    
    
    image_18.setImage(image1)
    image_19.setImage(image2)
    # keep track of which components have finished
    trial_4Components = [image_17, image_18, image_19]
    for thisComponent in trial_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_4" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_17* updates
        if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_17.frameNStart = frameN  # exact frame index
            image_17.tStart = t  # local t and not account for scr refresh
            image_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
            image_17.setAutoDraw(True)
        if image_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_17.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_17.tStop = t  # not accounting for scr refresh
                image_17.frameNStop = frameN  # exact frame index
                image_17.setAutoDraw(False)
        # Run 'Each Frame' code from code_6
        keys = selected.getKeys(keyList=["right", "left"], waitRelease=True)
        
        if keys:
            continueRoutine = False
        
        # *image_18* updates
        if image_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_18.frameNStart = frameN  # exact frame index
            image_18.tStart = t  # local t and not account for scr refresh
            image_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_18.started')
            image_18.setAutoDraw(True)
        if image_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_18.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_18.tStop = t  # not accounting for scr refresh
                image_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_18.stopped')
                image_18.setAutoDraw(False)
        
        # *image_19* updates
        if image_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_19.frameNStart = frameN  # exact frame index
            image_19.tStart = t  # local t and not account for scr refresh
            image_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_19.started')
            image_19.setAutoDraw(True)
        if image_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_19.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_19.tStop = t  # not accounting for scr refresh
                image_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_19.stopped')
                image_19.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_4" ---
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    
    arrow_y = -0.16
    
    if keys:
        if keys[-1] == "right":
            arrow_x = 0.4
        elif keys[-1] == "left":
            arrow_x = -0.4
    else:
        arrow_x = 5
    
    image_9.setImage(image1)
    image_10.setImage(image2)
    image_11.setPos((arrow_x, arrow_y))
    image_11.setImage('arrow.png')
    # keep track of which components have finished
    trial_2Components = [image_8, image_9, image_10, image_11]
    for thisComponent in trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_2" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_8* updates
        if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_8.frameNStart = frameN  # exact frame index
            image_8.tStart = t  # local t and not account for scr refresh
            image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
            image_8.setAutoDraw(True)
        if image_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_8.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_8.tStop = t  # not accounting for scr refresh
                image_8.frameNStop = frameN  # exact frame index
                image_8.setAutoDraw(False)
        
        # *image_9* updates
        if image_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            image_9.setAutoDraw(True)
        if image_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_9.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_9.tStop = t  # not accounting for scr refresh
                image_9.frameNStop = frameN  # exact frame index
                image_9.setAutoDraw(False)
        
        # *image_10* updates
        if image_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_10.frameNStart = frameN  # exact frame index
            image_10.tStart = t  # local t and not account for scr refresh
            image_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
            image_10.setAutoDraw(True)
        if image_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_10.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_10.tStop = t  # not accounting for scr refresh
                image_10.frameNStop = frameN  # exact frame index
                image_10.setAutoDraw(False)
        
        # *image_11* updates
        if image_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_11.frameNStart = frameN  # exact frame index
            image_11.tStart = t  # local t and not account for scr refresh
            image_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
            image_11.setAutoDraw(True)
        if image_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_11.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_11.tStop = t  # not accounting for scr refresh
                image_11.frameNStop = frameN  # exact frame index
                image_11.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_2" ---
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "trial_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    import random
    left_img = image1
    right_img = image2
    choice = ""
    if keys:
        choice = keys[-1].name
    
    def prob(present_case):
        p = [0, 0]
        value1 = random.randint(1, 4)
        value2 = random.randint(1, 4)
        if value1 > 1:
            p[0] = 1
        if value2 == 1:
            p[1] = 1
        if present_case%2 != 0:
            temp = p[0]
            p[0] = p[1]
            p[1] = temp
        return p
    
    if choice:
        error_msg = null
        p = prob(present_case)
    
        if present_case < 2:
            probability1 = 1 if p[0] == 0 else 0
            probability2 = 1 if p[1] == 0 else 0
        else:
            probability1 = p[0]
            probability2 = p[1]
        #["case","image1", "probability1", "image2", "probability2", "user_choice", "score"]
    
        rowdata = [cases[present_case], img1, probability1, img2, probability2, choice, score]
        writer.writerow(rowdata)
    
        if present_case == 0:
            if (choice == "right" and p[1] == 0) or (choice == "left" and p[0] == 0):
                curr_sound = "reward.wav"
                score += 1
            left_img = img_arr[p[0]]
            right_img = img_arr[p[1]]
        elif present_case == 1:
            if choice == "right":
                if p[1] == 0:
                    curr_sound = "reward.wav"
                    score += 1
                right_img = img_arr[p[1]]
                left_img = null
            elif choice == "left":
                if p[0] == 0:
                    curr_sound = "reward.wav"
                    score += 1
                left_img = img_arr[p[0]]
                right_img = null
        elif present_case == 2:
            if (choice == "right" and p[1] == 1) or (choice == "left" and p[0] == 1):
                curr_sound = "curse.wav"
                score -= 1
            left_img = img_arr[1 + p[0]]
            right_img = img_arr[1 + p[1]]
        elif present_case == 3:
            if choice == "right":
                if p[1] == 1:
                    curr_sound = "curse.wav"
                    score -= 1
                right_img = img_arr[1 + p[1]]
                left_img = null
            elif choice == "left":
                if p[0] == 1:
                    curr_sound = "curse.wav"
                    score -= 1
                left_img = img_arr[1 + p[0]]
                right_img = null
    else:
        error_msg = "error.png"
    image_13.setImage(left_img)
    image_14.setImage(right_img)
    sound_3.setSound(curr_sound, secs=1.5, hamming=True)
    sound_3.setVolume(1.0, log=False)
    image_15.setPos((arrow_x, arrow_y))
    image_15.setImage('arrow.png')
    image_29.setImage(error_msg)
    # keep track of which components have finished
    trial_3Components = [image_12, image_13, image_14, sound_3, image_15, image_29]
    for thisComponent in trial_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_3" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_12* updates
        if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            image_12.setAutoDraw(True)
        if image_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_12.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image_12.tStop = t  # not accounting for scr refresh
                image_12.frameNStop = frameN  # exact frame index
                image_12.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                image_13.setAutoDraw(False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                image_14.setAutoDraw(False)
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play(when=win)  # sync with win flip
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                sound_3.stop()
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_15.started')
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_15.stopped')
                image_15.setAutoDraw(False)
        
        # *image_29* updates
        if image_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_29.frameNStart = frameN  # exact frame index
            image_29.tStart = t  # local t and not account for scr refresh
            image_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_29.started')
            image_29.setAutoDraw(True)
        if image_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_29.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image_29.tStop = t  # not accounting for scr refresh
                image_29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_29.stopped')
                image_29.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_3" ---
    for thisComponent in trial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_3
    curr_sound = "null.wav"
    selected.clearEvents(eventType='keyboard')
    sound_3.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
# completed 16.0 repeats of 'trials'


# --- Prepare to start Routine "reset_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
reset_2Components = []
for thisComponent in reset_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "reset_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in reset_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "reset_2" ---
for thisComponent in reset_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "reset_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "main_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
sound_7.setSound('reality.wav', hamming=True)
sound_7.setVolume(1.0, log=False)
# keep track of which components have finished
main_instructionsComponents = [image_7, key_resp_4, Instructions_Main_4, continu_4, sound_7]
for thisComponent in main_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "main_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_4.started')
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Instructions_Main_4* updates
    if Instructions_Main_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Main_4.frameNStart = frameN  # exact frame index
        Instructions_Main_4.tStart = t  # local t and not account for scr refresh
        Instructions_Main_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Main_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_Main_4.started')
        Instructions_Main_4.setAutoDraw(True)
    
    # *continu_4* updates
    if continu_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        continu_4.frameNStart = frameN  # exact frame index
        continu_4.tStart = t  # local t and not account for scr refresh
        continu_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continu_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continu_4.started')
        continu_4.setAutoDraw(True)
    # start/stop sound_7
    if sound_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_7.frameNStart = frameN  # exact frame index
        sound_7.tStart = t  # local t and not account for scr refresh
        sound_7.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sound_7.started', tThisFlipGlobal)
        sound_7.play(when=win)  # sync with win flip
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in main_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "main_instructions" ---
for thisComponent in main_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
sound_7.stop()  # ensure sound has stopped at end of routine
# the Routine "main_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Rounds" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sound_6.setSound('rounds.wav', hamming=True)
    sound_6.setVolume(1.0, log=False)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    Instructions_Main_7.setText("Round"+str(rounds)+"/4")
    # Run 'Begin Routine' code from code_9
    rounds += 1
    # keep track of which components have finished
    RoundsComponents = [sound_6, image_24, key_resp_7, Instructions_Main_7, continu_6]
    for thisComponent in RoundsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Rounds" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_6
        if sound_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.tStart = t  # local t and not account for scr refresh
            sound_6.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_6.started', tThisFlipGlobal)
            sound_6.play(when=win)  # sync with win flip
        
        # *image_24* updates
        if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_24.frameNStart = frameN  # exact frame index
            image_24.tStart = t  # local t and not account for scr refresh
            image_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_24.started')
            image_24.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_Main_7* updates
        if Instructions_Main_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Main_7.frameNStart = frameN  # exact frame index
            Instructions_Main_7.tStart = t  # local t and not account for scr refresh
            Instructions_Main_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Main_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Main_7.started')
            Instructions_Main_7.setAutoDraw(True)
        
        # *continu_6* updates
        if continu_6.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continu_6.frameNStart = frameN  # exact frame index
            continu_6.tStart = t  # local t and not account for scr refresh
            continu_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continu_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continu_6.started')
            continu_6.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RoundsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Rounds" ---
    for thisComponent in RoundsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_6.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    trials_3.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        trials_3.addData('key_resp_7.rt', key_resp_7.rt)
    # the Routine "Rounds" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=96.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial_4" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_6
        import random
        from psychopy.hardware import keyboard
        
        
        if number%4 == 0:
            order = []
            while len(order) < 4:
                temp = random.randint(0, 3)
                if temp not in order:
                    order.append(temp)
        
        number += 1
        present_case = order[number%4]
        
        maybe = random.randint(0, 50)
        
        if(maybe%3):
            image1 = pairs[present_case][0]
            image2 = pairs[present_case][1]
        else:
            image1 = pairs[present_case][1]
            image2 = pairs[present_case][0]
        
        img1 = image1
        img2 = image2
        
        image1 = str(image1) + ".png"
        image2 =  str(image2) + ".png"
        
        selected = keyboard.Keyboard(bufferSize=1)
        selected.clearEvents(eventType='keyboard')
        
        loop += 1
        #print(keys[0].name)
        
        
        
        
        
        image_18.setImage(image1)
        image_19.setImage(image2)
        # keep track of which components have finished
        trial_4Components = [image_17, image_18, image_19]
        for thisComponent in trial_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_4" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_17* updates
            if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_17.frameNStart = frameN  # exact frame index
                image_17.tStart = t  # local t and not account for scr refresh
                image_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
                image_17.setAutoDraw(True)
            if image_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_17.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    image_17.tStop = t  # not accounting for scr refresh
                    image_17.frameNStop = frameN  # exact frame index
                    image_17.setAutoDraw(False)
            # Run 'Each Frame' code from code_6
            keys = selected.getKeys(keyList=["right", "left"], waitRelease=True)
            
            if keys:
                continueRoutine = False
            
            # *image_18* updates
            if image_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_18.frameNStart = frameN  # exact frame index
                image_18.tStart = t  # local t and not account for scr refresh
                image_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_18.started')
                image_18.setAutoDraw(True)
            if image_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_18.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    image_18.tStop = t  # not accounting for scr refresh
                    image_18.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_18.stopped')
                    image_18.setAutoDraw(False)
            
            # *image_19* updates
            if image_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_19.frameNStart = frameN  # exact frame index
                image_19.tStart = t  # local t and not account for scr refresh
                image_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_19.started')
                image_19.setAutoDraw(True)
            if image_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_19.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    image_19.tStop = t  # not accounting for scr refresh
                    image_19.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_19.stopped')
                    image_19.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_4" ---
        for thisComponent in trial_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # --- Prepare to start Routine "trial_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        
        arrow_y = -0.16
        
        if keys:
            if keys[-1] == "right":
                arrow_x = 0.4
            elif keys[-1] == "left":
                arrow_x = -0.4
        else:
            arrow_x = 5
        
        image_9.setImage(image1)
        image_10.setImage(image2)
        image_11.setPos((arrow_x, arrow_y))
        image_11.setImage('arrow.png')
        # keep track of which components have finished
        trial_2Components = [image_8, image_9, image_10, image_11]
        for thisComponent in trial_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_2" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_8* updates
            if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                image_8.setAutoDraw(True)
            if image_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_8.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_8.tStop = t  # not accounting for scr refresh
                    image_8.frameNStop = frameN  # exact frame index
                    image_8.setAutoDraw(False)
            
            # *image_9* updates
            if image_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                image_9.setAutoDraw(True)
            if image_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_9.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_9.tStop = t  # not accounting for scr refresh
                    image_9.frameNStop = frameN  # exact frame index
                    image_9.setAutoDraw(False)
            
            # *image_10* updates
            if image_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                image_10.setAutoDraw(True)
            if image_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_10.tStop = t  # not accounting for scr refresh
                    image_10.frameNStop = frameN  # exact frame index
                    image_10.setAutoDraw(False)
            
            # *image_11* updates
            if image_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_11.frameNStart = frameN  # exact frame index
                image_11.tStart = t  # local t and not account for scr refresh
                image_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                image_11.setAutoDraw(True)
            if image_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_11.tStop = t  # not accounting for scr refresh
                    image_11.frameNStop = frameN  # exact frame index
                    image_11.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_2" ---
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "trial_3" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        import random
        left_img = image1
        right_img = image2
        choice = ""
        if keys:
            choice = keys[-1].name
        
        def prob(present_case):
            p = [0, 0]
            value1 = random.randint(1, 4)
            value2 = random.randint(1, 4)
            if value1 > 1:
                p[0] = 1
            if value2 == 1:
                p[1] = 1
            if present_case%2 != 0:
                temp = p[0]
                p[0] = p[1]
                p[1] = temp
            return p
        
        if choice:
            error_msg = null
            p = prob(present_case)
        
            if present_case < 2:
                probability1 = 1 if p[0] == 0 else 0
                probability2 = 1 if p[1] == 0 else 0
            else:
                probability1 = p[0]
                probability2 = p[1]
            #["case","image1", "probability1", "image2", "probability2", "user_choice", "score"]
        
            rowdata = [cases[present_case], img1, probability1, img2, probability2, choice, score]
            writer.writerow(rowdata)
        
            if present_case == 0:
                if (choice == "right" and p[1] == 0) or (choice == "left" and p[0] == 0):
                    curr_sound = "reward.wav"
                    score += 1
                left_img = img_arr[p[0]]
                right_img = img_arr[p[1]]
            elif present_case == 1:
                if choice == "right":
                    if p[1] == 0:
                        curr_sound = "reward.wav"
                        score += 1
                    right_img = img_arr[p[1]]
                    left_img = null
                elif choice == "left":
                    if p[0] == 0:
                        curr_sound = "reward.wav"
                        score += 1
                    left_img = img_arr[p[0]]
                    right_img = null
            elif present_case == 2:
                if (choice == "right" and p[1] == 1) or (choice == "left" and p[0] == 1):
                    curr_sound = "curse.wav"
                    score -= 1
                left_img = img_arr[1 + p[0]]
                right_img = img_arr[1 + p[1]]
            elif present_case == 3:
                if choice == "right":
                    if p[1] == 1:
                        curr_sound = "curse.wav"
                        score -= 1
                    right_img = img_arr[1 + p[1]]
                    left_img = null
                elif choice == "left":
                    if p[0] == 1:
                        curr_sound = "curse.wav"
                        score -= 1
                    left_img = img_arr[1 + p[0]]
                    right_img = null
        else:
            error_msg = "error.png"
        image_13.setImage(left_img)
        image_14.setImage(right_img)
        sound_3.setSound(curr_sound, secs=1.5, hamming=True)
        sound_3.setVolume(1.0, log=False)
        image_15.setPos((arrow_x, arrow_y))
        image_15.setImage('arrow.png')
        image_29.setImage(error_msg)
        # keep track of which components have finished
        trial_3Components = [image_12, image_13, image_14, sound_3, image_15, image_29]
        for thisComponent in trial_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_3" ---
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_12* updates
            if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_12.frameNStart = frameN  # exact frame index
                image_12.tStart = t  # local t and not account for scr refresh
                image_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                image_12.setAutoDraw(True)
            if image_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_12.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_12.tStop = t  # not accounting for scr refresh
                    image_12.frameNStop = frameN  # exact frame index
                    image_12.setAutoDraw(False)
            
            # *image_13* updates
            if image_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_13.frameNStart = frameN  # exact frame index
                image_13.tStart = t  # local t and not account for scr refresh
                image_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
                image_13.setAutoDraw(True)
            if image_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_13.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_13.tStop = t  # not accounting for scr refresh
                    image_13.frameNStop = frameN  # exact frame index
                    image_13.setAutoDraw(False)
            
            # *image_14* updates
            if image_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_14.frameNStart = frameN  # exact frame index
                image_14.tStart = t  # local t and not account for scr refresh
                image_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
                image_14.setAutoDraw(True)
            if image_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_14.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_14.tStop = t  # not accounting for scr refresh
                    image_14.frameNStop = frameN  # exact frame index
                    image_14.setAutoDraw(False)
            # start/stop sound_3
            if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_3.frameNStart = frameN  # exact frame index
                sound_3.tStart = t  # local t and not account for scr refresh
                sound_3.tStartRefresh = tThisFlipGlobal  # on global time
                sound_3.play(when=win)  # sync with win flip
            if sound_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_3.tStop = t  # not accounting for scr refresh
                    sound_3.frameNStop = frameN  # exact frame index
                    sound_3.stop()
            
            # *image_15* updates
            if image_15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_15.frameNStart = frameN  # exact frame index
                image_15.tStart = t  # local t and not account for scr refresh
                image_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_15.started')
                image_15.setAutoDraw(True)
            if image_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_15.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_15.tStop = t  # not accounting for scr refresh
                    image_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_15.stopped')
                    image_15.setAutoDraw(False)
            
            # *image_29* updates
            if image_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_29.frameNStart = frameN  # exact frame index
                image_29.tStart = t  # local t and not account for scr refresh
                image_29.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_29, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_29.started')
                image_29.setAutoDraw(True)
            if image_29.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_29.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_29.tStop = t  # not accounting for scr refresh
                    image_29.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_29.stopped')
                    image_29.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_3" ---
        for thisComponent in trial_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_3
        curr_sound = "null.wav"
        selected.clearEvents(eventType='keyboard')
        sound_3.stop()  # ensure sound has stopped at end of routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        thisExp.nextEntry()
        
    # completed 96.0 repeats of 'trials_2'
    
# completed 4.0 repeats of 'trials_3'


# --- Prepare to start Routine "End_Screen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
sound_4.setSound('post.wav', hamming=True)
sound_4.setVolume(1.0, log=False)
# keep track of which components have finished
End_ScreenComponents = [image_16, key_resp_5, sound_4, Instructions_Main_5, continu_5]
for thisComponent in End_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End_Screen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_16* updates
    if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_16.frameNStart = frameN  # exact frame index
        image_16.tStart = t  # local t and not account for scr refresh
        image_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_16.started')
        image_16.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_5.started')
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_4
    if sound_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_4.frameNStart = frameN  # exact frame index
        sound_4.tStart = t  # local t and not account for scr refresh
        sound_4.tStartRefresh = tThisFlipGlobal  # on global time
        sound_4.play(when=win)  # sync with win flip
    
    # *Instructions_Main_5* updates
    if Instructions_Main_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Main_5.frameNStart = frameN  # exact frame index
        Instructions_Main_5.tStart = t  # local t and not account for scr refresh
        Instructions_Main_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Main_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_Main_5.started')
        Instructions_Main_5.setAutoDraw(True)
    
    # *continu_5* updates
    if continu_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        continu_5.frameNStart = frameN  # exact frame index
        continu_5.tStart = t  # local t and not account for scr refresh
        continu_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continu_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continu_5.started')
        continu_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End_Screen" ---
for thisComponent in End_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
sound_4.stop()  # ensure sound has stopped at end of routine
# the Routine "End_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=112.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial_7" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_10
    import random
    from psychopy.hardware import keyboard
    
    
    
    
    number += 1
    present_case = random.choice(post_learn)
    to_delete_index = post_learn.index(present_case)
    post_learn.pop(to_delete_index)
    
    maybe = random.randint(1, 51)
    
    if(maybe%3):
        image1 = present_case[0]
        image2 = present_case[1]
    else:
        image1 = present_case[1]
        image2 = present_case[0]
    
    img1 = image1
    img2 = image2
    
    image1 = str(image1) + ".png"
    image2 =  str(image2) + ".png"
    
    selected = keyboard.Keyboard(bufferSize=1)
    selected.clearEvents(eventType='keyboard')
    
    loop += 1
    #print(keys[0].name)
    
    
    
    
    
    image_32.setImage(image1)
    image_33.setImage(image2)
    # keep track of which components have finished
    trial_7Components = [image_31, image_32, image_33]
    for thisComponent in trial_7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_7" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_31* updates
        if image_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_31.frameNStart = frameN  # exact frame index
            image_31.tStart = t  # local t and not account for scr refresh
            image_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_31, 'tStartRefresh')  # time at next scr refresh
            image_31.setAutoDraw(True)
        if image_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_31.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_31.tStop = t  # not accounting for scr refresh
                image_31.frameNStop = frameN  # exact frame index
                image_31.setAutoDraw(False)
        # Run 'Each Frame' code from code_10
        keys = selected.getKeys(keyList=["right", "left"], waitRelease=True)
        
        if keys:
            continueRoutine = False
        
        # *image_32* updates
        if image_32.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_32.frameNStart = frameN  # exact frame index
            image_32.tStart = t  # local t and not account for scr refresh
            image_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_32, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_32.started')
            image_32.setAutoDraw(True)
        if image_32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_32.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_32.tStop = t  # not accounting for scr refresh
                image_32.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_32.stopped')
                image_32.setAutoDraw(False)
        
        # *image_33* updates
        if image_33.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_33.frameNStart = frameN  # exact frame index
            image_33.tStart = t  # local t and not account for scr refresh
            image_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_33.started')
            image_33.setAutoDraw(True)
        if image_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_33.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_33.tStop = t  # not accounting for scr refresh
                image_33.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_33.stopped')
                image_33.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_7" ---
    for thisComponent in trial_7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "trial_6" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_8
    
    arrow_y = -0.16
    
    if keys:
        if keys[-1] == "right":
            arrow_x = 0.4
        elif keys[-1] == "left":
            arrow_x = -0.4
    else:
        arrow_x = 5
    
    image_26.setImage(image1)
    image_27.setImage(image2)
    image_28.setPos((arrow_x, arrow_y))
    image_28.setImage('arrow.png')
    # keep track of which components have finished
    trial_6Components = [image_25, image_26, image_27, image_28]
    for thisComponent in trial_6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_6" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_25* updates
        if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_25.frameNStart = frameN  # exact frame index
            image_25.tStart = t  # local t and not account for scr refresh
            image_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
            image_25.setAutoDraw(True)
        if image_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_25.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_25.tStop = t  # not accounting for scr refresh
                image_25.frameNStop = frameN  # exact frame index
                image_25.setAutoDraw(False)
        
        # *image_26* updates
        if image_26.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_26.frameNStart = frameN  # exact frame index
            image_26.tStart = t  # local t and not account for scr refresh
            image_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
            image_26.setAutoDraw(True)
        if image_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_26.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_26.tStop = t  # not accounting for scr refresh
                image_26.frameNStop = frameN  # exact frame index
                image_26.setAutoDraw(False)
        
        # *image_27* updates
        if image_27.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_27.frameNStart = frameN  # exact frame index
            image_27.tStart = t  # local t and not account for scr refresh
            image_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_27, 'tStartRefresh')  # time at next scr refresh
            image_27.setAutoDraw(True)
        if image_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_27.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_27.tStop = t  # not accounting for scr refresh
                image_27.frameNStop = frameN  # exact frame index
                image_27.setAutoDraw(False)
        
        # *image_28* updates
        if image_28.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_28.frameNStart = frameN  # exact frame index
            image_28.tStart = t  # local t and not account for scr refresh
            image_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_28.started')
            image_28.setAutoDraw(True)
        if image_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_28.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_28.tStop = t  # not accounting for scr refresh
                image_28.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_28.stopped')
                image_28.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_6" ---
    for thisComponent in trial_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "error" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_11
    import random
    import time
    left_img = image1
    right_img = image2
    choice = ""
    if keys:
        choice = keys[-1].name
    
    
    if choice:
        error_msg = null
        rowdata = [present_case, img1,  img2, choice ]
        writer.writerow(rowdata)
    else:
        error_msg = "error.png"
        
     
    image_34.setImage(error_msg)
    # keep track of which components have finished
    errorComponents = [image_30, image_34]
    for thisComponent in errorComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "error" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_30* updates
        if image_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_30.frameNStart = frameN  # exact frame index
            image_30.tStart = t  # local t and not account for scr refresh
            image_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_30, 'tStartRefresh')  # time at next scr refresh
            image_30.setAutoDraw(True)
        if image_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_30.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_30.tStop = t  # not accounting for scr refresh
                image_30.frameNStop = frameN  # exact frame index
                image_30.setAutoDraw(False)
        
        # *image_34* updates
        if image_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_34.frameNStart = frameN  # exact frame index
            image_34.tStart = t  # local t and not account for scr refresh
            image_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_34, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_34.started')
            image_34.setAutoDraw(True)
        if image_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_34.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_34.tStop = t  # not accounting for scr refresh
                image_34.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_34.stopped')
                image_34.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in errorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "error" ---
    for thisComponent in errorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_11
    curr_sound = "null.wav"
    selected.clearEvents(eventType='keyboard')
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 112.0 repeats of 'trials_4'


# --- Prepare to start Routine "Final_Score_and_Good_Bye" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
sound_5.setSound('end.wav', secs=60, hamming=True)
sound_5.setVolume(1.0, log=False)
# keep track of which components have finished
Final_Score_and_Good_ByeComponents = [image_23, key_resp_6, sound_5, Instructions_Main_6]
for thisComponent in Final_Score_and_Good_ByeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Final_Score_and_Good_Bye" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_23* updates
    if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_23.frameNStart = frameN  # exact frame index
        image_23.tStart = t  # local t and not account for scr refresh
        image_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_23.started')
        image_23.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['r'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_5
    if sound_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_5.frameNStart = frameN  # exact frame index
        sound_5.tStart = t  # local t and not account for scr refresh
        sound_5.tStartRefresh = tThisFlipGlobal  # on global time
        sound_5.play(when=win)  # sync with win flip
    if sound_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_5.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            sound_5.tStop = t  # not accounting for scr refresh
            sound_5.frameNStop = frameN  # exact frame index
            sound_5.stop()
    
    # *Instructions_Main_6* updates
    if Instructions_Main_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Main_6.frameNStart = frameN  # exact frame index
        Instructions_Main_6.tStart = t  # local t and not account for scr refresh
        Instructions_Main_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Main_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_Main_6.started')
        Instructions_Main_6.setAutoDraw(True)
    if Instructions_Main_6.status == STARTED:  # only update if drawing
        Instructions_Main_6.setText("Absolutely! Thank you for playing our game. We hope you had a great time exploring the mysteries of ancient Egypt and uncovering hidden treasures.\n\nNow, without further ado, we are pleased to present your final score:\n\n"+str(score)+"\n\nWe hope you enjoyed playing the game as much as we enjoyed creating it. We appreciate your participation and feedback.\n\nThank you again for playing, and best of luck on all your future quests! Goodbye!"
, log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Final_Score_and_Good_ByeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Final_Score_and_Good_Bye" ---
for thisComponent in Final_Score_and_Good_ByeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
sound_5.stop()  # ensure sound has stopped at end of routine
# the Routine "Final_Score_and_Good_Bye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from code_5
output_file.close()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
