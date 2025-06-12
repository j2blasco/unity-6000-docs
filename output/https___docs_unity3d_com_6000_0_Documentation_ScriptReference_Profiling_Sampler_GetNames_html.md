* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.GetNames.html

#  [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html).GetNames
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
public static int GetNames(List<string> names); 
### Parameters
Parameter | Description  
---|---  
names | Preallocated list the Sampler names are written to. Or _null_ if you want to get number of Samplers only.  
### Returns
**int** Number of active Samplers. 
### Description
Returns number and names of all registered Profiler labels.
Use **GetNames** to get a number of available Samplers and fill the _names_ list parameter with their names.  
  
**Note:** At the moment all built-in counters are available only in the Editor and Development Players. **GetNames** in non-Development Players returns returns 0 and empty list.
* * *
