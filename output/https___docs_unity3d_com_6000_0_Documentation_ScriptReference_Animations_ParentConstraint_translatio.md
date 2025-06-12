* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ParentConstraint-translationAxis.html

#  [ParentConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ParentConstraint.html).translationAxis
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
[Animations.Axis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.Axis.html) translationAxis; 
### Description
The translation axes affected by the ParentConstraint.
Use this property to restrict the translation of the constrained object on a particular axis.
```
using UnityEngine.Animations;  
  
public class ConstraintAxis
{
    public void ConstrainOnlyOnXY(ParentConstraint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ParentConstraint.html) component)
    {
        component.translationAxis = Axis.X[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.Axis.X.html) | Axis.Y[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.Axis.Y.html);
    }
}

```

* * *
