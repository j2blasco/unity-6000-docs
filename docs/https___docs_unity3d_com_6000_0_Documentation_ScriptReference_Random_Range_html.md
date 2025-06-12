* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html

#  [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html).Range
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
## Declaration
public static float Range(float minInclusive, float maxInclusive); 
### Description
Returns a random `float` within `[minInclusive..maxInclusive]` (range is inclusive).
If `minInclusive` is greater than `maxInclusive`, then the numbers are automatically swapped.  
  
**Important** : Both the lower and upper bounds are **inclusive**. Any given float value between them, _including both minInclusive and maxInclusive_ , will appear on average approximately once every ten million random samples.  
  
There is an `int` overload of this function that operates slightly differently, especially regarding the range maximum. See its docs below.  
  
See [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html) for details on the algorithm, and for examples of how `UnityEngine.Random` may be different from other random number generators. 
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefab;  
  
    // Click the "Instantiate!" button and a new `prefab` will be instantiated
    // somewhere within -10.0 and 10.0 (inclusive) on the x-z plane
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 50), "Instantiate!"))
        {
            var position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-10.0f, 10.0f), 0, Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-10.0f, 10.0f));
            Instantiate(prefab, position, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
        }
    }
}

```

* * *
## Declaration
public static int Range(int minInclusive, int maxExclusive); 
### Description
Return a random `int` within `[minInclusive..maxExclusive)` (Read Only).
The maximum parameter is exclusive, so for example `Random.Range(0, 10)` returns a value between 0 and 9, each with approximately equal probability.  
  
If `minInclusive` and `maxExclusive` are equal, the method returns `minInclusive`.  
  
If `minInclusive` is greater than `maxExclusive`, the input parameters are swapped but retain their inclusivity or exclusivity based on their original positions, which means the method becomes `Random.Range(minExclusive, maxInclusive)` after swapping.  
  
For example, calling `Random.Range(10, 0)` is not equivalent to `Random.Range(0, 10)`. `Random.Range(10, 0)` returns a value between 1 and 10 because 10 becomes an inclusive maximum and 0 becomes an exclusive minimum.  
  
There is a `float` overload of this function that operates slightly differently, especially regarding the range maximum, refer to its docs above.  
  
Refer to [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html) for details on the algorithm, and for examples of how `UnityEngine.Random` may differ from other random number generators. 
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefab;
    public float zoffset = 10;  
  
    // Click the "Instantiate!" button and a new grid of `prefab` objects will be
    // instantiated with a random number of items in each direction.
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 50), "Instantiate!"))
        {
            // the grid will always be 1, 2, 3, 4, or 5 prefabs wide
            int xcount = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(1, 6);
            // the grid will always be 2, 3, or 4 prefabs long
            int ycount = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(2, 5);  
  
            for (int x = 0; x != xcount; ++x)
            {
                for (int y = 0; y != ycount; ++y)
                {
                    var position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(x * 2, zoffset, y * 2);
                    Instantiate(prefab, position, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
                }
            }  
  
            zoffset += 2;
        }
    }
}

```

* * *
