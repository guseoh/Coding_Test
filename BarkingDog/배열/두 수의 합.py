# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

# 풀이 1: 브루트 포스
# 무차별 대입 방식
def twoSum(self, nums: list[int], taget: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == taget:
                return [i, j]

# 풀이 2: in을 이용한 탐색
# 모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫 번째 값을 뺀 값 target - n 이 존재하는 탐색
def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums): # enumerate(): 인덱스와 원소로 이루어진 튜플을 만들어준다. 
        complement = target - n
        
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1].__index__(complement) + i + 1]

# 풀이 3: 첫번째 수를 뺀 결과 키 조회
def twoSum(self, nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
