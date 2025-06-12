* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime.html

# MediaTime
struct in UnityEditor.Media
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
Time representation for use with media containers.
A [MediaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime.html) can be thought of as "sample #`count` at `rate` Hz".  
  
This representation is precise, even for large values, because the sample count and rate are stored separately and do not make use of floating point storage.
### Static Properties
Property | Description  
---|---  
[Invalid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime.Invalid.html) | Invalid time value.  
### Properties
Property | Description  
---|---  
[count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime-count.html) | The sample count for the time value.  
[rate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime-rate.html) | The rate used for converting the count into seconds.  
### Constructors
Constructor | Description  
---|---  
[MediaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime-ctor.html) | Creates a time value with an integer number of seconds, using 1Hz for the rate.  
### Operators
Operator | Description  
---|---  
[double](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime-operator_double.html) | Returns the time value expressed as a floating point number of seconds.  
* * *
