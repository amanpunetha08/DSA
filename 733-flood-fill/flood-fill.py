class Solution:
    def dfs(self,sr,sc,n,m,color,image,starting_color):
        if sr <0 or sr >=n or sc <0 or sc >=m or image[sr][sc] != starting_color:
            return
        
        image[sr][sc] = color

        self.dfs(sr+1,sc,n,m,color,image,starting_color)
        self.dfs(sr-1,sc,n,m,color,image,starting_color)
        self.dfs(sr,sc+1,n,m,color,image,starting_color)
        self.dfs(sr,sc-1,n,m,color,image,starting_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        starting_color = image[sr][sc]
        if starting_color == color:
            return image

        self.dfs(sr,sc,n,m,color,image,starting_color)
        return image
        