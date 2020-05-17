def shth(sx, sy, mose):
    wit = len(mose[0])
    hit = len(mose)
    Brd = [[None for i in range(wit)] for i in range(hit)]
    Brd[sx][sy] = 1

    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
          nx, ny = x + i[0], y + i[1]
          if 0 <= nx < hit and 0 <= ny < wit:
            if Brd[nx][ny] is None:
                Brd[nx][ny] = Brd[x][y] + 1
                if mose[nx][ny] == 1:
                  continue
                arr.append((nx, ny))

    return Brd


def solution(mose):
  wit = len(mose[0])
  hit = len(mose)
  tb = shth(0, 0, mose)
  bt = shth(hit-1, wit-1, mose)
  Brd = []

  ans = 2 ** 32-1
  for i in range(hit):
      for j in range(wit):
          if tb[i][j] and bt[i][j]:
              ans = min(tb[i][j] + bt[i][j] - 1, ans)
  return ans