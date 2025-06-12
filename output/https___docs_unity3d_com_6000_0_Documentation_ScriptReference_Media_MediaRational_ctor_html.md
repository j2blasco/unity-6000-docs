* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaRational-ctor.html

# MediaRational Constructor
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
public MediaRational(int numerator); 
## Declaration
public MediaRational(int numerator, int denominator); 
### Parameters
Parameter | Description  
---|---  
numerator | Numerator of the rational number.  
denominator | Denominator of the rational number.  
### Description
Constructs a rational number. The version that omits the denominator sets it to 1.
Rationals created with constructors produce a normalized value. For example, passing in 2 and 4 results in the rational having 1 and 2 for its numerator and denominator, respectively.
* * *
