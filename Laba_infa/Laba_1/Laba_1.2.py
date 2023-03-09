import numpy as np
import matplotlib.pyplot as plt
import math
import os
import xlrd3
from scipy.interpolate import make_interp_spline, BSpline
import pandas as pd

# plt.scatter(x,y,s=2, c='red') - отображает отдельные точки, s=size, c=colour


def mnq(x, y, xerrr, yerrr, xlabel, ylabel, label='', k=0, b=0):
    """
    Строит прямую по методу наименьших квадратов.
    :param x: экспериментальные данные по х
    :param y: экспериментальные данные по у
    :param xlabel: подпись оси х
    :param ylabel: подпись оси y
    :param k: теор прямая
    :param b: теор прямая

    """
    global u
    polynom, error = np.polyfit(x, y, deg=1, cov=True)
    polynom_function = np.poly1d(polynom)
    # plt.errorbar(x, y, xerr=xerrr, yerr=yerrr, fmt='r.')
    plt.scatter(x, y, s=3, c='green')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    maxi = max(x)
    plt.plot(x, polynom_function(x), label=label + str(polynom_function))

    if k != 0 or b != 0:
        plt.plot(x, k * x + b)
    plt.grid()
    plt.legend(loc='best', fontsize=12)

    print(polynom_function(0.15))
    print("Уравнение для экспериментальной кривой номер ", str(u), " y = kx + b:",
          'y = {}x + {}'.format(polynom_function[1], polynom_function[0]))
    print("Погрешность для k: " + str((error[0][0]) ** 0.5))
    print("Погрешность для b: " + str((error[1, 1]) ** 0.5))
    plt.show()


def mnq_add(x, y, xerrr, yerrr, label=''):
    global u
    polynom, error = np.polyfit(x, y, deg=1, cov=True)
    polynom_function = np.poly1d(polynom)
    plt.errorbar(x, y, xerr=xerrr, yerr=yerrr, fmt='r.')
    plt.scatter(x, y, s=3, c='green')
    plt.plot(x, polynom_function(x), label=label + str(polynom_function))
    print("Уравнение для экспериментальной кривой номер ", str(u), " y = kx + b:",
          'y = {}x + {}'.format(polynom_function[1], polynom_function[0]))
    print("Погрешность для k: " + str((error[0][0]) ** 0.5))
    print("Погрешность для b: " + str((error[1, 1]) ** 0.5))
    u += 1


def TableV(path, Nrows, Ncolums):
    workbook = xlrd3.open_workbook(path)

    worksheet = workbook.sheet_by_index(0)
    # Iterate the rows and columns
    data = []
    for i in range(Ncolums):
        data.append([])
    for i in range(Ncolums):
        for j in range(1, Nrows):
            # Print the cell values with tab space
            data[i].append(worksheet.cell_value(j, i))
    return data


def TableG(path, Nrows, Ncolums):
    workbook = xlrd3.open_workbook(path)

    worksheet = workbook.sheet_by_index(0)
    # Iterate the rows and columns
    data = [[], []]
    for i in range(Nrows):
        for j in range(1, Ncolums):
            # Print the cell values with tab space
            data[i].append(worksheet.cell_value(i, j))
    return data


# !!!массив для x должен быть отсортирован по возрастанию!!!
def curve(x, y, xer, yer, xlabel, ylabel, label=''):
    x = np.array(x)
    y = np.array(y)

    # define x as 200 equally spaced values between the min and max of original x
    xnew = np.linspace(x. min(), x. max(), 200)

    # define spline
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(xnew)

    # create smooth line chart
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.errorbar(x, y, xerr=xer, yerr=yer)
    plt.grid()

    plt.plot(xnew, y_smooth, label=label)
    # plt.scatter(x, y, c = 'red')
    plt.legend(loc='best', fontsize=12)

    plt.show()


def add_curve(x, y, xer, yer, label=''):
    x = np.array(x)
    y = np.array(y)

    # define x as 200 equally spaced values between the min and max of original x
    xnew = np.linspace(x. min(), x. max(), 200)

    # define spline
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(xnew)

    # create smooth line chart
    # plt.errorbar(x, y, xerr=xer, yerr=yer) # fmt='r.' чтобы точки были поверх кривой
    # plt.scatter(x, y, c = 'red')
    plt.plot(xnew, y_smooth, label=label)


u = 1


data = TableV(os.getcwd() + '/test.xlsx', 102, 2)
er = []


for i in range(len(data)):
    er.append(0)

mnq(data[0], data[1], er, er, 'Размер массива',
    'Время выполнения поиска, мc', '')
