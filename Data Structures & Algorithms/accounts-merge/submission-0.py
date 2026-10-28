class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailgraph = defaultdict(list)
        emailname = {}
        for acct in accounts:
            first = acct[1]
            for email in acct[1:]:
                emailgraph[first].append(email)
                emailgraph[email].append(first)
                emailname[email] = acct[0]
        seen = set()
        merged = []
        for email in emailname:
            if email in seen:
                continue
            seen.add(email)
            stack = [email]
            group = []
            while stack: 
                node = stack.pop()
                group.append(node)
                for nxt in emailgraph[node]:
                    if nxt not in seen:
                        seen.add(nxt)
                        stack.append(nxt)
            merged.append([emailname[email]] + sorted(group))
        return merged




#do it using dfs