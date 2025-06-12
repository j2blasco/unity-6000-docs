* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.GetSide.html

#  [Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html).GetSide
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
## Declaration
public bool GetSide([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point); 
### Description
Is a point on the positive side of the plane?
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) goalLine1;
    public Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) goalLine2;
    public Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) leftSideLine;
    public Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) rightSideLine;  
  
    int GoalScored(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ballPos)
    {
        // If the ball is within the sidelines...
        if (!leftSideLine.GetSide(ballPos) && !rightSideLine.GetSide(ballPos))
        {
            // If the ball is over goal line 1 then it's a goal for team 1...
            if (goalLine1.GetSide(ballPos))
            {
                return 1;
            }
            // ...else if the ball is over goal line 2 then it's a goal for team 2.
            else if (goalLine2.GetSide(ballPos))
            {
                return 2;
            }
        }  
  
        // Otherwise, it isn't a goal for either team.
        return 0;
    }
}

```

* * *
