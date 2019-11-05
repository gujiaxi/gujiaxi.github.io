---
layout: post
title: "在main()前/后调用函数"
date: 2012-05-21 23:04
---
分别通过使用GCC的扩展和C++的constructor这两种守法在main()的前面/后面调用函数的方法。

## 在main()前面调用函数
可用`__attribute__((constructor))`扩展功能在GCC中定义在main()前被呼叫的函数。
```c
#include <stdio.h>
__attribute__((constructor))
void foo() {
    printf("hello, before main\n");
}
int main() {
    printf("hello, world\n");
    return 0;
}
```

运行结果如下：
```shell
$ ./a.out
hello, before main
hello, world
```

上面的`__attribute__((constructor))`是GCC的扩展功能所以没有移植性。然而，在C++中通过使用class的constructor却能用可移植方法进行同样的操作。
```c
#include <stdio.h>
void foo() {
    printf("hello, before main\n");
}
namespace { struct foo_caller { foo_caller() { foo(); }} caller; }
int main() {
    printf("hello, world\n");
    return 0;
}
```

## 在main()后面调用函数
相对的：
```c
#include <stdio.h>
void foo() {
    printf("hello, before main\n");
}
namespace { struct foo_caller { ~foo_caller() { foo(); }} caller; }
int main() {
    printf("hello, world\n");
    return 0;
}
```
