"""
In a 2 dimensional array grid, each value grid[i][j] represents the
height of a building located there. We are allowed to increase the height
of any number of buildings, by any amount (the amounts can be different for
different buildings). Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid,
i.e. top, bottom, left, and right, must be the same as the skyline of the
original grid. A city's skyline is the outer contour of the rectangles
formed by all the buildings when viewed from a distance.
See the following example.

What is the maximum total sum that the height of the
buildings can be increased?

Notes:
1 < grid.length = grid[0].length <= 50.
All heights grid[i][j] are in the range [0, 100].
All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.
"""

class Solution(object):

   def main():
      my_grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
      print(maxIncreaseKeepingSkyline(my_grid))

   def maxIncreaseKeepingSkyline(self, grid):
      """
      :type grid: List[List[int]]
      :rtype: int
      """
      top_bottom_skyline = self.getTopBottomView(grid)
      left_right_skyline = self.getLeftRightView(grid)

      print(top_bottom_skyline)
      print(left_right_skyline)

   def sumOfGrid(self, grid):
      sum = 0
      for building_height in grid:
         sum += building_height

   def getTopBottomView(self, grid):
      list = []
      for index in range(len(grid[0])):
         largest_element = -1
         for array in grid:
            if array[index] > largest_element:
               largest_element = array[index]
         list.append(largest_element)
      return list

   def getLeftRightView(self, grid):
      list = []
      for array in grid:
         list.append(max(array))
      return list
