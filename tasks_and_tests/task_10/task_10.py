from __future__ import annotations
from typing import Any


class PowerSet:
    def __init__(self) -> None:
        self.set = {}

    def size(self) -> int:
        return len(self.set)

    def put(self, value: Any) -> None:
        if not self.set.get(value):
            self.set[value] = value

    def get(self, value: Any) -> bool:
        if self.set.get(value) is not None:
            return True
        return False

    def remove(self, value: Any) -> bool:
        if self.set.get(value) is not None:
            del self.set[value]
            return True
        return False

    def intersection(self, set2: PowerSet) -> PowerSet:
        ans = PowerSet()
        if self.size() < set2.size():
            set1, set2 = self, set2
        else:
            set1, set2 = set2, self

        for i in set1.set.values():
            if set2.get(i) is True:
                ans.put(i)

        return ans

    def union(self, set2: PowerSet) -> PowerSet:
        ans = PowerSet()
        for i in self.set.values():
            ans.put(i)

        for i in set2.set.values():
            ans.put(i)

        return ans

    def difference(self, set2: PowerSet) -> PowerSet:
        ans = PowerSet()
        for i in self.set.values():
            if set2.get(i) is False:
                ans.put(i)

        return ans

    def issubset(self, set2: PowerSet) -> bool:
        for i in set2.set.values():
            if self.get(i) is False:
                return False
        return True

    def equals(self, set2: PowerSet) -> bool:
        if self.size() != set2.size():
            return False

        for i in self.set.values():
            if set2.get(i) is False:
                return False
        return True
