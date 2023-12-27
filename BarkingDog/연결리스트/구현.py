class Node:
    def __init__(self, data, address=None):
        self.data = data
        self.address = address # 노드 안에는 데이터와 주소 값이 있다.
    
    def addData(data):
        node = head
        # 주소값이 없어질 때 까지 루프(마지막 노드 탐색)
        while node.address:
            node = node.address
        node.address = Node(data)


# 노드는 first와 sec 각각 값이 들어가며, 주소값은 설정을 하지 않았다면 디폴트로 None이 삽입
firstNode= Node('first')
secNode = Node('sec')

# 첫째 노드의 주소값을 둘째 노드로 지정하면서 둘이 연결된다.
firstNode.address = secNode

# 첫째 노드를 head(처음노드)로 지정해야 다른 노드들을 찾을 수 있다.
head = firstNode