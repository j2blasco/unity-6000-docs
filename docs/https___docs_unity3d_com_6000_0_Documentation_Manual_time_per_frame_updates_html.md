* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/time-per-frame-updates.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Managing time and frame rate](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html)
  * Per-frame updates


[](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html)
Managing time and frame rate
[](https://docs.unity3d.com/6000.0/Documentation/Manual/fixed-updates.html)
Fixed updates
# Per-frame updates
Unity performs some updates once per frame. Your MonoBehaviour **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) can hook into this update loop through the [`MonoBehaviour.Update`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) method. For example, in your game character’s `Update` method, you might read the user input from a joypad, and move the character forward a certain amount. It’s important to remember when handling time-based actions like this that the game’s frame rate can vary and so the length of time between `Update` calls also varies.
The variable frame rate of a game is often expressed in **frames per second** The frequency at which consecutive frames are displayed in a running game. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#framespersecond), or **FPS** See first person shooter, frames per second.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FPS). Frame rate varies according to factors like the capabilities of the host device and the complexity of the graphics and computation required to draw each frame. For example, your game may run at a slower frame rate when there are 100 active, on-screen characters than when there is only one.
Unless otherwise constrained by your [quality settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) or by the [Adaptive Performance package](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.adaptiveperformance.html), Unity tries to run your game at the fastest frame rate possible. You can see more details of what occurs each frame in the **Game Logic** section of the [execution order diagram](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html).
Consider the task of moving an object forward gradually, one frame at a time. It might seem at first that you could just translate the object by a fixed distance each frame:
```
//C# script example
using UnityEngine;
using System.Collections;

public class ExampleScript : MonoBehaviour {
    public float distancePerFrame;
    
    void Update() {
        transform.Translate(0, 0, distancePerFrame); // this is incorrect
    }
}

```

However with this code, as the frame rate varies, the object’s apparent speed also varies. If the game is running at 100 FPS, the object moves `distancePerFrame` 100 times per second. But if the frame rate slows to 60 FPS (due to CPU load, for example) then it only steps forward 60 times per second and therefore covers a shorter distance over the same amount of time.
In most cases this is undesirable, particularly with games and animation. It’s much more common to want your in-game objects to move at steady and predictable speeds regardless of the frame rate. The solution is to scale the amount of movement each frame by the amount of time elapsed each frame, which you can read from the [Time.deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) property:
```
//C# script example
using UnityEngine;
using System.Collections;

public class ExampleScript : MonoBehaviour {
    public float distancePerSecond;
    
    void Update() {
        transform.Translate(0, 0, distancePerSecond * Time.deltaTime);
    }
}

```

Note that the movement is now given as `distancePerSecond` rather than `distancePerFrame`. As the frame rate varies, the size of the movement step will vary accordingly and so the object’s speed will be constant.
Depending on your target platform, use either [Application.targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html) or [QualitySettings.vSyncCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-vSyncCount.html) to set the frame rate of your application. For more information, see the [Application.targetFrameRate API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html).
## Additional resources
  * [Fixed updates](https://docs.unity3d.com/6000.0/Documentation/Manual/fixed-updates.html)
  * [Handling variations in time](https://docs.unity3d.com/6000.0/Documentation/Manual/time-handling-variations.html)
  * [In-game versus real time](https://docs.unity3d.com/6000.0/Documentation/Manual/time-scale.html)
  * [Capture frame rate](https://docs.unity3d.com/6000.0/Documentation/Manual/time-capture-frame-rate.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html)
Managing time and frame rate
[](https://docs.unity3d.com/6000.0/Documentation/Manual/fixed-updates.html)
Fixed updates
