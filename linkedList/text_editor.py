class TextEditor:
    def __init__(self):
        self.docs = {}
        self.cursor_pos = [None, 0]

    def init(self, name):
        self.docs[name] = ""
        self.cursor_pos = [name, 0]

    def move(self, name):
        self.cursor_pos = [name, 0]

    def insert(self, text):
        doc_name = self.cursor_pos[0]
        cursor_idx = self.cursor_pos[1]

        self.docs[doc_name] = (
            self.docs[doc_name][:cursor_idx] + text + self.docs[doc_name][cursor_idx:]
        )
        self.cursor_pos[1] += len(text)
        print(len(self.docs[doc_name]))

    def erase(self, cnt):
        doc_name = self.cursor_pos[0]
        cursor_idx = self.cursor_pos[1]

        if cursor_idx == 0:
            print("nothing")
            return

        cnt = min(cnt, cursor_idx)

        erased_text = self.docs[doc_name][cursor_idx - cnt : cursor_idx]
        self.docs[doc_name] = (
            self.docs[doc_name][: cursor_idx - cnt] + self.docs[doc_name][cursor_idx:]
        )

        self.cursor_pos[1] -= cnt
        if not erased_text:
            print("nothing")
        else:
            print(erased_text[::-1])

    def cursor(self, cnt):
        doc_name = self.cursor_pos[0]
        cursor_idx = self.cursor_pos[1]
        prev_cursor_idx = cursor_idx

        new_cursor_idx = cursor_idx + cnt
        if new_cursor_idx < 0:
            new_cursor_idx = 0
        elif new_cursor_idx > len(self.docs[doc_name]):
            new_cursor_idx = len(self.docs[doc_name])

        self.cursor_pos[1] = new_cursor_idx

        if prev_cursor_idx == new_cursor_idx:
            print("nothing")
        elif prev_cursor_idx < new_cursor_idx:
            print(self.docs[doc_name][prev_cursor_idx:new_cursor_idx])
        else:
            print(self.docs[doc_name][new_cursor_idx:prev_cursor_idx][::-1])

    def merge(self, name1, name2):
        self.docs[name1] += self.docs[name2]
        del self.docs[name2]
        self.cursor_pos = [name1, 0]
        print(len(self.docs[name1]))


q = int(input())
editor = TextEditor()

for _ in range(q):
    command, *args = input().split()

    if command == "init":
        editor.init(args[0])
    elif command == "move":
        editor.move(args[0])
    elif command == "insert":
        editor.insert(args[0])
    elif command == "erase":
        editor.erase(int(args[0]))
    elif command == "cursor":
        editor.cursor(int(args[0]))
    elif command == "merge":
        editor.merge(args[0], args[1])
