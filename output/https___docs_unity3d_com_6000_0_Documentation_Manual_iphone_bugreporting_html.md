* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-bugreporting.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
  * [Test and debug an iOS application](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-testing-and-debugging.html)
  * Report crash bugs for iOS


[](https://docs.unity3d.com/6000.0/Documentation/Manual/TroubleShootingIPhone.html)
Troubleshooting on iOS devices
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-performance.html)
Optimize performance for iOS
# Report crash bugs for iOS
You can report crash bugs for iOS with Unity [Bug Reporting](https://unity.com/releases/editor/qa/bug-reporting). If your application crashes in the Xcode debugger, it’s recommended to add the Xcode console output to your bug report. Use the following steps to access the console output if your application crashes:
**Note** : Before submitting a [bug report](https://unity.com/releases/editor/qa/bug-reporting), refer to [Troubleshooting on iOS devices](https://docs.unity3d.com/6000.0/Documentation/Manual/TroubleShootingIPhone.html) where you will find solutions to common crashes and other problems.
  1. From the **Debug** menu , select **Continue** twice.
  2. Open the debugger console from **View** > **Debug Area** > **Activate Console**.
  3. In the console, type `thread backtrace all` and press **Enter**.
  4. Copy the console output and attach it to your bug report.


When reporting any application freezes, you can click **Pause** and repeat the previous steps.
If your application crashes on the iOS device, it’s recommended to retrieve the crash report. To achieve this, refer to [Acquiring Crash and Low Memory Reports](https://developer.apple.com/library/archive/technotes/tn2151/_index.html#//apple_ref/doc/uid/DTS40008184-CH1-ACQUIRING_CRASH_AND_LOW_MEMORY_REPORTS) (Apple Developer). Attach the crash report, your built application, and the console log to your bug report.
## Additional resources
  * [Troubleshooting on iOS devices](https://docs.unity3d.com/6000.0/Documentation/Manual/TroubleShootingIPhone.html)
  * [Bug reporting](https://unity.com/releases/editor/qa/bug-reporting)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TroubleShootingIPhone.html)
Troubleshooting on iOS devices
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-performance.html)
Optimize performance for iOS
