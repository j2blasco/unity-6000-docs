* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Index_operator.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).this[int,int]
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
this[int,int]; 
### Description
Access element at [row, column].
Both `row` and `column` must be from 0 to 3 inclusive. A matrix is 4x4 array of numbers, and you can access the individual elements using this function.  
  
Note the standard math notation - row is the first index.
* * *
this[int]; 
### Description
Access element at sequential index (0..15 inclusive).
A matrix is 4x4 array of numbers (16 numbers in total). You can access the individual elements using "flattened" index with this. The `index` is `row+column*4`.
* * *
