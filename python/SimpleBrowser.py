from StackMy import Stack

class Browser:
    def __init__(self, step_length):
        self.forward_stack = Stack(step_length)
        self.backward_stack = Stack(step_length)

    def can_back(self):
        if self.backward_stack.index > 0:
            return True
        else:
            return False

    def can_forward(self):
        if self.forward_stack.index > 0:
            return True
        else:
            return False

    def back(self):
        if self.can_back() and self.backward_stack.index > 1:
            ret = self.backward_stack.pop()
            self.forward_stack.push(ret)
            return self.backward_stack.array[self.backward_stack.index-1]

    def forward(self):
        if self.can_forward():
            ret = self.forward_stack.pop()
            self.backward_stack.push(ret)
            return ret

    def browse_url(self, url):
        self.backward_stack.push(url)


def main():
    browser_my = Browser(10)
    url_list = ["baidu.com", "163.com", "battle.net", "zhihu.com", "google.com", "taobao.com"]
    for url in url_list:
        browser_my.browse_url(url)
    print(browser_my.back())
    print(browser_my.back())
    print(browser_my.back())
    print(browser_my.forward())
    print(browser_my.forward())
    print(browser_my.back())
    print(browser_my.back())
    print(browser_my.forward())
    print(browser_my.forward())
    print(browser_my.forward())
    print(browser_my.forward())
    print(browser_my.back())
    print(browser_my.back())
    print(browser_my.back())
    print(browser_my.back())
    print(browser_my.back())
    print(browser_my.back())
    print(browser_my.back())

if __name__ == "__main__":
    main()