* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * Using common math functions


[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)
Moving objects with vectors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-random.html)
Using randomness
# Using common math functions
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html "Go to Mathf page in the Scripting Reference")
Unity’s Mathf class provides a collection of common math functions, including trigonometric, logarithmic, and other functions commonly required in games and app development.
This page provides an overview of the Mathf class and its common uses when scripting with it. For an exhaustive reference of every member of the Mathf class, see the [Mathf script reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).
## Trigonometric
All Unity’s trigonometry functions work in **radians**. 
  * [`Sin`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)
  * [`Cos`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)
  * [`Tan`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Tan.html)
  * [`Asin`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Asin.html)
  * [`Acos`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Acos.html)
  * [`Atan`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Atan.html)
  * [`Atan2`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Atan2.html)


[`PI`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html) is available as a constant, and you can multiply by the static values [`Rad2Deg`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Rad2Deg.html) or [`Deg2Rad`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html) to convert between radians and degrees.
## Powers and Square Roots
Unity provides the common power and square root functions you would expect: - [`Pow`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Pow.html) - [`Sqrt`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sqrt.html) - [`Exp`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Exp.html)
As well as some useful power-of-two related functions. These are useful when working with common binary data sizes, which are often constrained or optimized to power-of-two values (such as texture dimensions):
  * [`ClosestPowerOfTwo`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.ClosestPowerOfTwo.html)
  * [`NextPowerOfTwo`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html)
  * [`IsPowerOfTwo`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.IsPowerOfTwo.html)


## Interpolation
Unity’s interpolation functions allows you to calculate a value that is some way between two given points. Each of these functions behaves in a different way, suitable for different situations. See the examples in each for more information:
  * [`Lerp`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html)
  * [`LerpAngle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpAngle.html)
  * [`LerpUnclamped`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpUnclamped.html)
  * [`InverseLerp`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.InverseLerp.html)
  * [`MoveTowards`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.MoveTowards.html)
  * [`MoveTowardsAngle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.MoveTowardsAngle.html)
  * [`SmoothDamp`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.SmoothDamp.html)
  * [`SmoothDampAngle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.SmoothDampAngle.html)
  * [`SmoothStep`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.SmoothStep.html)


Note that the [Vector classes](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html) and the [`Quaternion`](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Quaternion.html) class all have their own interpolation functions (such as Quaternion.Lerp) which allow you to interpolate positions, directions and rotations in multiple dimensions.
## Limiting and repeating values
These simple helper functions are often useful in games or apps and can save you time when you need to limit values to a certain range or repeat them within a certain range.
  * [`Max`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Max.html) and [`Min`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Min.html)
  * [`Repeat`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Repeat.html) and [`PingPong`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)
  * [`Clamp`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp.html) and [`Clamp01`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp01.html)
  * [`Ceil`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Ceil.html) and [`Floor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Floor.html)


## Logarithmic
The [`Log`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html) function allows you to calculate the logarithm of a specified number, either the natural logarithm or in a specified base. Additionally the [`Log10`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log10.html) function returns the base–10 logarithm of the specified number.
## Other functions
For the full list of functions in the Mathf class, see the [Mathf script reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).
Mathf
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)
Moving objects with vectors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-random.html)
Using randomness
