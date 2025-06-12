* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html

# ExpressionEvaluator
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
### Description
Evaluates simple math expressions; supports int / float and operators: + - * / % ^ ( ).
This class has a single generic static method [Evaluate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.Evaluate.html), that evaluates a mathematical expression and returns the result.  
  
Supported number types are: `int`, `float`, `long`, `double`.  
  
The expressions that can be evaluated support:
  * arithmetic operators `a+b`, `a-b`, `a*b`, `a/b`,
  * power (`a^b`) and modulo (`a%b`) operators,
  * parentheses,
  * math functions `sqrt(a)`, `floor(a)`, `ceil(a)`, `round(a)`,
  * trigonometic functions `cos(a)`, `sin(a)`, `tan(a)` (argument expressed in radians), and a constant `pi`.


```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Int Expression")]
    public static void IntExample()
    {
        ExpressionEvaluator.Evaluate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.Evaluate.html)("2+3", out int result);
        // prints 5
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(result);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Float Expression")]
    public static void FloatExample()
    {
        ExpressionEvaluator.Evaluate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.Evaluate.html)("sqrt(cos(pi/3))", out float result);
        // prints 0.7071068
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(result);
    }
}

```

### Static Methods
Method | Description  
---|---  
[Evaluate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.Evaluate.html) | Evaluates a math expression and returns the result.  
* * *
