# Advent of Code 2020

This is a repository for learning from master xiang.

- 看布爷代码赏心悦目
第六题原来就是union和intersection竟然都没有发现实在是太菜了。

- 为什么题目一天比一天傻屌
- day11 题目太难了，实在不会做，只能暴力算了。 等向师来找个规律

以后开始还是要写一个简单的思路来记录菜鸡的我，不然感觉题目白做了！

## Day 17

暴力模拟！ 因为要求比较苛刻所以最终active状态的点不会很多， 而且只会循环六轮， 所以模拟有两种选择：
1. 用数组模拟， 我们知道只会循环6轮，因此我们可以定义数组大小为 size+12 
2. 用集合和队列模拟， 记录下所有active点的坐标，然后每一次根据active点的坐标来扩展队列。（速度更快，因为需要检查的点会少很多）

## Day 18

字符串匹配： 每个左括号都会对应一个右括号，当左括号出现时可以递归开始先计算左括号内的数字，由于递归，最后出现的左括号一定是会和最先出现的右括号匹配，不用担心多个括号匹配错误。