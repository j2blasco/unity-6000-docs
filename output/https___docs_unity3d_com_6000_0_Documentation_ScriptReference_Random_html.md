* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html

# Random
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-random.html "Go to Random Component in the Manual")
### Description
Easily generate random data for games.
This static class provides several easy game-oriented ways of generating [pseudorandom numbers](https://en.wikipedia.org/wiki/Pseudorandomness).  
  
The generator is an [Xorshift 128](http://en.wikipedia.org/wiki/Xorshift) algorithm, based on the paper [Xorshift RNGs](http://www.jstatsoft.org/v08/i14/paper) by George Marsaglia. It is statically initialized with a high-[entropy](https://en.wikipedia.org/wiki/Entropy_\(information_theory\)) [seed](https://en.wikipedia.org/wiki/Random_seed) from the operating system, and stored in native memory where it will survive domain reloads. This means that the generator is seeded exactly once on process start, and after that is left entirely under script control.  
  
For more details on the seed, including how to manage it yourself, see [InitState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.InitState.html). To learn how to save and restore the state of [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html), see [state](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-state.html).  
  
**Versus System.Random**  
  
This class has the same name as the .NET Framework class [System.Random](https://docs.microsoft.com/en-us/dotnet/api/system.random) and serves a similar purpose, but differs in some key ways:  
  
_Static vs instanced_  
`UnityEngine.Random` is a static class, and so its state is globally shared. Getting random numbers is easy, because there is no need to `new` an instance and manage its storage. However, static state is problematic when working with threads or jobs (the generator will error if used outside the main thread), or if multiple independent random number generators are required. In those cases, managing instances of `System.Random` would be a better option.  
  
_Float upper bounds are inclusive_  
All properties and methods in `UnityEngine.Random` that work with or derive work from float-based randomness (for example [value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html) or [ColorHSV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.ColorHSV.html)) will use an _inclusive_ upper bound. This means that it is possible, though as rare as any other given value, for the max to be randomly returned. In contrast, `System.Random.NextDouble()` has an _exclusive_ maximum, and will never return the maximum value, but only a number slightly below it.  
  
_Performance_  
Methods in `UnityEngine.Random` have been measured to be between 20% and 40% faster than their equivalents in `System.Random`.  
  
_Name resolution ambiguity_  
Because the classes share the name `Random`, it can be easy to get a [CS0104](https://docs.microsoft.com/en-us/dotnet/csharp/misc/cs0104) "ambiguous reference" compiler error if the `System` and `UnityEngine` namespaces are both brought in via `using`. To disambiguate, either use an alias `using Random = UnityEngine.Random;`, fully-qualify the typename e.g. `UnityEngine.Random.InitState(123);`, or eliminate the `using System` and fully-qualify or alias types from that namespace instead.  
  

### Static Properties
Property | Description  
---|---  
[insideUnitCircle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitCircle.html) | Returns a random point inside or on a circle with radius 1.0 (Read Only).  
[insideUnitSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitSphere.html) | Returns a random point inside or on a sphere with radius 1.0 (Read Only).  
[onUnitSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-onUnitSphere.html) | Returns a random point on the surface of a sphere with radius 1.0 (Read Only).  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotation.html) | Returns a random rotation (Read Only).  
[rotationUniform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotationUniform.html) | Returns a random rotation with uniform distribution (Read Only).  
[state](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-state.html) | Gets or sets the full internal state of the random number generator.  
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html) | Returns a random float within [0.0..1.0] (range is inclusive) (Read Only).  
### Static Methods
Method | Description  
---|---  
[ColorHSV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.ColorHSV.html) | Generates a random color from HSV and alpha ranges.  
[InitState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.InitState.html) | Initializes the random number generator state with a seed.  
[Range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html) | Returns a random float within [minInclusive..maxInclusive] (range is inclusive).  
* * *
