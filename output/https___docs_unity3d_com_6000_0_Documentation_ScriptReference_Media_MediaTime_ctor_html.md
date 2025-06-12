* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime-ctor.html

# MediaTime Constructor
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
public MediaTime(long seconds); 
### Parameters
Parameter | Description  
---|---  
seconds | The number of seconds in the time value.  
### Description
Creates a time value with an integer number of seconds, using 1Hz for the rate.
* * *
## Declaration
public MediaTime(long count, uint rateNumerator, uint rateDenominator); 
### Parameters
Parameter | Description  
---|---  
count | The sample count for the time value.  
rateNumerator | Numerator for the rate used by the time value.  
rateDenominator | Denominator for the rate used by the time value.  
### Description
Creates a time value for a specified sample count and rate.
* * *
