#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import argparse,logging,sys,itertools
from datetime import datetime
from libs.configurations import Configuration
from libs.dbcontroller import *
from libs.models import *
from sqlalchemy import *

controller = SessionController()
#link de la referencia https://fahrenheitfreiheit.wordpress.com/2018/05/06/el-problema-de-las-n-reinas-i/

def check_legal(board):
    legal = True
    for i, ci in enumerate(board):
        for cj in board[(i + 1):]:
            if abs(ci - cj) == abs(board.index(ci) - board.index(cj)):
                legal = False
    return legal

    
def check_n_queens(n):
    session = controller.getSession()
    result=[]
    nq = n
    try:
        for i in range(1, n + 1):
            n_board = list(range(1, i + 1))
            configs = itertools.permutations(n_board)
            count = 0
            for board in configs:
                if check_legal(board):
                    if len(board) == nq:
                        result.append(board)
                    count += 1
        logging.info(f'{n} Reinas | {count} Soluciones')
        logging.info(f"Fila del tablero y el valor la columna {result}")
        row = insert(SolutionsNQueens).values({'n_queens':n,'solutions':count,\
            'positions':result})
        session.execute(row)
        session.commit()
    except Exception as e:
        logging.info(f'Error is {e}')
        
    return result
    


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-q","--queens",help="number of queens",type=int, default=1)
        args = parser.parse_args()
        
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
        logger = logging.getLogger()

        controller.createTables()

        if args.queens > 0:
            check_n_queens(args.queens)
         
    except Exception as e:
        logging.error(f"Process terminated with error: {e}")
        raise


if __name__ == '__main__':
    main()
