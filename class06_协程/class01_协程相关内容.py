"""
@Time ： 2024-06-12 09:35
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：协程
"""

import asyncio

'''
协程&asyncio&异步编程
    协程不是计算机提供，程序员人为创造。
    协程(Coroutine)，也可以被称为微线程，是一种用户态内的上下文切换技术。简而言之，其实就是通过一个线程实现代码块相互切换执行。

实现协程有这么几种方法
    1.yield关键字。
    2.async、await关键字(py3.5)【推荐】

意义：在一个线程中如果遇到10等待时间，线程不会傻傻等，利用空闲的时候再去干点其他事。
    
'''

'''
异步编程：
事件循环：理解成一个死循环，去检测执行某些代码
    # 生成或获取一个事件循环
    loop=asyncio.get_event_loop()
    # 任务放到任务列表中
    loop.run_until_complete(任务)
    
    简化：asyncio.run(任务)
    
    协程函数：async def 函数名(参数):
    协程对象：执行 协程函数(参数) 得到的协程对象
        执行协程函数创建协程对象，函数内部不会执行，必须将协程对象交给事件循环处理
        例子：
            async def func():
                pass
            result=func()
            asyncio.run(result)
    

'''


# await + 可等待的对象(协程对象、Future对象、Task对象 - -->IO等待)
# await: 等待对象的值得到结果再继续向下走

async def func1():
    print('func1 start')
    await asyncio.sleep(2)
    print('func1 end')


async def func2():
    print('func2 start')
    await asyncio.sleep(2)
    print('func2 end')


async def main1():
    print('main start')

    # 遇到IO操作挂起当前协程任务，等IO操作完成之后再往下继续执行。
    # 当前协程挂起时，继续执行其他协程任务。
    await func2()
    await func1()

    print('main end')


asyncio.run(main1())

print('*' * 100)
'''
Task对象：

白话:在事件循环中添加多个任务的，

Tasks用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象，这样可以让协程加入事件
循环中等待被调度执行。
'''


async def func3():
    print('func3 start')
    await asyncio.sleep(2)
    print('func3 end')
    return 'func3'


async def func4():
    print('func4 start')
    await asyncio.sleep(2)
    print('func4 end')
    return 'func4'


async def main2():
    print('main2 start')
    task_list = [
        asyncio.create_task(func3(), name='这是任务对象func3'),
        asyncio.create_task(func4(), name='这是任务对象func4'),
    ]

    print('main2 end')
    # 等待多个异步操作（协程或 Future 对象）中的一个或多个完成。这个函数允许你在异步编程中进行并发操作，同时等待多个任务的结果
    done, pending = await asyncio.wait(task_list)
    print(done)
    return 'main2'


asyncio.run(main2())
