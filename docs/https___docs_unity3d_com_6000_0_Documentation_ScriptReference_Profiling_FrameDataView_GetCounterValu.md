* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCounterValuePtr.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetCounterValuePtr
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
public void* GetCounterValuePtr(int markerId); 
### Parameters
Parameter | Description  
---|---  
markerId | Marker identifier.  
### Returns
**void*** Returns unsafe pointer to the counter value. 
### Description
Gets unsafe pointer to the last value of a counter marker in the frame.
Use to retrieve a pointer to the last data sample of a marker with [MarkerFlags.Counter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.Counter.html) flag.
```
using UnityEditor.Profiling;  
  
class Example
{
    static unsafe bool TryExtractMyCounterValue(FrameDataView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html) frameData, string counterName, out int counterValue)
    {
        var counterMarkerId = frameData.GetMarkerId(counterName);
        void* valuePtr = frameData.GetCounterValuePtr(counterMarkerId);
        if (valuePtr == null)
        {
            counterValue = 0;
            return false;
        }  
  
        counterValue = *(int*)valuePtr;
        return true;
    }
}

```

**Note:**   
If no data was produced for the counter in the frame, the return value is null.
* * *
