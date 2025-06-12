* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * Managing time and frame rate


[](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
Object-oriented development
[](https://docs.unity3d.com/6000.0/Documentation/Manual/time-per-frame-updates.html)
Per-frame updates
# Managing time and frame rate
It’s important to understand how Unity handles time to ensure your gameplay remains stable. Updates occur at regular time intervals to capture changes to character positions, health status, scores, and so on. If your code makes changes in the wrong update loop or doesn’t allow for variations in time, effects like movement might be too fast, too slow, or jumpy instead of smooth.
The `Time` class contains properties through which you can get and in some cases set various time-related measurements and settings. Refer to [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) in the Scripting API reference for a complete list of the properties and their meanings.
**Topic** | **Description**  
---|---  
[Per-frame updates](https://docs.unity3d.com/6000.0/Documentation/Manual/time-per-frame-updates.html) | Updates which happen once per frame and whose frequency therefore depends on frame rate.  
[Fixed updates](https://docs.unity3d.com/6000.0/Documentation/Manual/fixed-updates.html) | Updates which happen at a configurable fixed time interval.  
[In-game time and real time](https://docs.unity3d.com/6000.0/Documentation/Manual/time-scale.html) | The configurable relationship between in-game time and real time and the potential effects.  
[Handling variation in time](https://docs.unity3d.com/6000.0/Documentation/Manual/time-handling-variations.html) | Techniques Unity uses to compensate for variations in time and frame rate and to limit the effects of one-time delays.  
[Capture frame rate](https://docs.unity3d.com/6000.0/Documentation/Manual/time-capture-frame-rate.html) | Compensating for frame rate when recording video of gameplay.  
## Additional resources
  * [Time API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html)
  * [Time settings in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TimeManager.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
Object-oriented development
[](https://docs.unity3d.com/6000.0/Documentation/Manual/time-per-frame-updates.html)
Per-frame updates
