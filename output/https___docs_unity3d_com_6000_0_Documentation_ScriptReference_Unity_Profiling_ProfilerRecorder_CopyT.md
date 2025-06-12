* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.CopyTo.html

#  [ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html).CopyTo
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
public int CopyTo(ProfilerRecorderSample* dest, int destSize, bool reset); 
### Parameters
Parameter | Description  
---|---  
dest | Pointer to the destination samples array.  
destSize | Destination samples array size.  
reset | Reset ProfilerRecorder.  
### Returns
**int** Returns the count of the copied elements. 
### Description
Copies collected samples to the destination array.
```
using Unity.Profiling;  
  
public class ExampleScript
{
    static double GetRecorderFrameAverage(ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) recorder)
    {
        var samplesCount = recorder.Capacity;
        if (samplesCount == 0)
            return 0;  
  
        double r = 0;
        unsafe
        {
            var samples = stackalloc ProfilerRecorderSample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorderSample.html)[samplesCount];
            recorder.CopyTo(samples, samplesCount);
            for (var i = 0; i < samplesCount; ++i)
                r += samples[i].Value;
            r /= samplesCount;
        }  
  
        return r;
    }
}

```

* * *
## Declaration
public void CopyTo(List<ProfilerRecorderSample> outSamples, bool reset); 
### Parameters
Parameter | Description  
---|---  
outSamples | Destination list.  
reset | Reset ProfilerRecorder.  
### Description
Copies all collected samples to the destination list.
* * *
