### 如何在函数计算中操作设备


1.	首先导入import iot

2. 	通过提供设备的ProductKey和DeviceName操作设备

3. 	操作设备包括setThingProperties，getThingProperties和callThingService。另外也提供了通过tag获取设备列表的getThingsWithTags，方便用户操作一系列设备。

4.	同时也提供了publish接口，方便用户发布消息

