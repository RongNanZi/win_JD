# 京东挑战赛规划

### 步骤一：数据去噪声

* 去除重复操作
	- 因为time属性是精确到秒的，所以按照userid,skuid,time作为key值过滤数据库
* 去除操作次数过多的用户
	- 次数设置什么样的阈值，我认为我们得先直观看下所用用户的操作次数，然后选择一个阈值，不能直接生搬硬套
* 去除对同一件商品操作次数过多的用户
	- 这个我感觉和上个一样，本来用检测离群点的方法来选会好点，但是时间有点紧还是直接按照上一个任务的一样

### 步骤二：构建特征
* 用户特征：
	- 用户总浏览量
	- 用户总购买量
	- 用户浏览购买转化率
* 品牌特征：
	- 品牌总浏览量
	- 品牌总销售量
	- 品牌浏览购买转化率
	- 品牌平均销售周期
* 用户-品牌特征：
	- 用户-品牌浏览行为次数
	- 用户-品牌关注行为次数
	- 用户-品牌购买总量
	- 用户-品牌购买行为次数
	- 用户-品牌最后操作日期

这些特征的具体描述在文章里都有
### 步骤三：构造模型
* 随机森林
	- 我看文章里的实验结果随机森林最好，那就做这个吧
* 神经网络
	- 神经网络可能会产生意想不到的效果

```
这两种方法最后结果做个比较
```


