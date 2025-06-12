* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-operator_subtract.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).operator -
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) operator -([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) a, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) b); 
### Returns
**Vector2** The difference between the two vectors, returned as a Vector2 struct. 
### Description
Subtracts one vector from another.
Subtracts each component of `b` from `a`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Create two vectors.
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) A = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 2);
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) B = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(3, 2);
        
        // Subtract vector B from vector A.
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) C = A - B;
        
        // Print the result.
        print(C);
    }
}

```

* * *
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) operator -([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) a); 
### Returns
**Vector2** The negative of the vector, returned as a Vector2 struct. 
### Description
Negates a vector.
Each component in the vector is negated, to obtain its negative value. The negative of a vector has the same magnitude but opposite direction
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
       // Create a vector.
       Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) A = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 2);
       
       // Find the negative value.
       Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) B = - A;
  
       // Print the result.
        print(B + " is the negative of " + A);
    }
}

```

* * *
