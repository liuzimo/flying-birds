#coding:utf-8
import pygame
import sys
def load():
    # 小鸟图片的载入路径
    PlayerPath = (
            './assets/sprites/redbird-upflap.png',
            './assets/sprites/redbird-midflap.png',
            './assets/sprites/redbird-downflap.png'
    )

    # 背景图片
    BackgroundPath = './assets/sprites/background-black.png'

    # 管道障碍物图片
    PipePath = './assets/sprites/pipe-green.png'

    Images = {}

    # 数字
    Images['numbers'] = (
        pygame.image.load('./assets/sprites/0.png').convert_alpha(),
        pygame.image.load('./assets/sprites/1.png').convert_alpha(),
        pygame.image.load('./assets/sprites/2.png').convert_alpha(),
        pygame.image.load('./assets/sprites/3.png').convert_alpha(),
        pygame.image.load('./assets/sprites/4.png').convert_alpha(),
        pygame.image.load('./assets/sprites/5.png').convert_alpha(),
        pygame.image.load('./assets/sprites/6.png').convert_alpha(),
        pygame.image.load('./assets/sprites/7.png').convert_alpha(),
        pygame.image.load('./assets/sprites/8.png').convert_alpha(),
        pygame.image.load('./assets/sprites/9.png').convert_alpha()
    )

    # 地面
    Images['base'] = pygame.image.load('./assets/sprites/base.png').convert_alpha()

    Sounds = {}

    # # 声音
    # if 'win' in sys.platform:
    #     soundExt = '.wav'
    # else:
    #     soundExt = '.ogg'

    # Sounds['die']    = pygame.mixer.Sound('./assets/audio/die' + soundExt)
    # Sounds['hit']    = pygame.mixer.Sound('./assets/audio/hit' + soundExt)
    # Sounds['point']  = pygame.mixer.Sound('./assets/audio/point' + soundExt)
    # Sounds['swoosh'] = pygame.mixer.Sound('./assets/audio/swoosh' + soundExt)
    # Sounds['wing']   = pygame.mixer.Sound('./assets/audio/wing' + soundExt)

    Images['background'] = pygame.image.load(BackgroundPath).convert()

    #随机选取小鸟的样子
    Images['player'] = (
        pygame.image.load(PlayerPath[0]).convert_alpha(),
        pygame.image.load(PlayerPath[1]).convert_alpha(),
        pygame.image.load(PlayerPath[2]).convert_alpha(),
    )

    # 选取管道障碍物
    Images['pipe'] = (
        pygame.transform.rotate(
            pygame.image.load(PipePath).convert_alpha(), 180),
        pygame.image.load(PipePath).convert_alpha(),
    )

    Hitmasks = {}

    Hitmasks['pipe'] = (
        getHitmask(Images['pipe'][0]),
        getHitmask(Images['pipe'][1]),
    )

    Hitmasks['player'] = (
        getHitmask(Images['player'][0]),
        getHitmask(Images['player'][1]),
        getHitmask(Images['player'][2]),
    )

    return Images, Sounds, Hitmasks

def getHitmask(image):
    mask = []
    for x in range(image.get_width()):
        mask.append([])
        for y in range(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask
