# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

# 풀이 1: 투 포인터
# 최대 높이의 막대까지 각각 좌우 기둥 최대 높이 left_max, right_max가 현재 높이와의
# 차이만큼 물 높이 volume을 더해 나간다.

def trap(Self, height: list[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
        return volume