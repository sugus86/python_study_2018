# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *


def main():
    # ��������
    screen = pygame.display.set_mode((480, 800))
    # ���ô�������
    pygame.display.set_caption("My Game")
    # ���� Clock ����
    clock = pygame.time.Clock()


    # ���������ͼ����Դ
    bg = pygame.image.load('images/background.png').convert()
    plane = pygame.image.load('images/plane.png').convert_alpha()

    # �����߼�����
    while True:
        # ����֡��Ϊ 30
        clock.tick(30)
        # ���Ʊ���
        screen.blit(bg, (0, 0))
        # ��ȡ�������
        (x, y) = pygame.mouse.get_pos()
        # �ֱ��ȡͼ����
        x -= plane.get_width() / 2
        y -= plane.get_height() / 2
        # ���Ʒɻ�
        screen.blit(plane, (x, y))

        # ���������¼�
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        # ���»���
        pygame.display.update()


if __name__ == '__main__':
    main()