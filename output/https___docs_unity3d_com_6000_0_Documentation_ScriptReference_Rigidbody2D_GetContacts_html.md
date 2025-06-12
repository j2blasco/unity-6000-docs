* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).GetContacts
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
public int GetContacts(ContactPoint2D[] contacts); 
### Parameters
Parameter | Description  
---|---  
contacts | An array of [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `contacts` array. 
### Description
Retrieves all contact points for all of the Collider(s) attached to this Rigidbody.
Contacts involving a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) set to be a trigger will never be returned here because trigger Colliders do not have contact points.  
  
When retrieving contacts, you should ensure that the provided array is large enough to contain all the contacts you are interested in. Typically the array would be reused therefore it would be a size to return a reasonable quantity of contacts. This function also means that no allocations occur which means no work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts(Collider2D[] colliders); 
### Parameters
Parameter | Description  
---|---  
colliders | An array of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
### Returns
**int** Returns the number of colliders placed in the `colliders` array. 
### Description
Retrieves all Colliders in contact with any of the Collider(s) attached to this Rigidbody.
When retrieving contacts, you should ensure that the provided array is large enough to contain all the contacts you are interested in. Typically the array would be reused therefore it would be a size to return a reasonable quantity of contacts. This function also means that no allocations occur which means no work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, ContactPoint2D[] contacts); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | An array of [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `contacts` array. 
### Description
Retrieves all contact points for all of the Collider(s) attached to this Rigidbody, with the results filtered by the `ContactFilter2D`.
Contacts involving a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) set to be a trigger will never be returned here because trigger Colliders do not have contact points. This is true even if the `contactFilter` has its [ContactFilter2D.useTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-useTriggers.html) set to true.  
  
When retrieving contacts, you should ensure that the provided array is large enough to contain all the contacts you are interested in. Typically the array would be reused therefore it would be a size to return a reasonable quantity of contacts. This function also means that no allocations occur which means no work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, Collider2D[] colliders); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
colliders | An array of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
### Returns
**int** Returns the number of colliders placed in the `colliders` array. 
### Description
Retrieves all Colliders in contact with any of the Collider(s) attached to this rigidbody, with the results filtered by the `ContactFilter2D`.
When retrieving contacts, you should ensure that the provided array is large enough to contain all the contacts you are interested in. Typically the array would be reused therefore it would be a size to return a reasonable quantity of contacts. This function also means that no allocations occur which means no work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts(List<ContactPoint2D> contacts); 
### Parameters
Parameter | Description  
---|---  
contacts | A list of [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `contacts` list. 
### Description
Retrieves all contact points for all of the Collider(s) attached to this Rigidbody.
Contacts involving a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) set to be a trigger will never be returned here because trigger Colliders do not have contact points.  
  
The integer return value is the number of results written into the `contacts` list. The contacts list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `contacts` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<ContactPoint2D> contacts); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | A list of [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `contacts` list. 
### Description
Retrieves all contact points for all of the Collider(s) attached to this Rigidbody.
Contacts involving a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) set to be a trigger will never be returned here because trigger Colliders do not have contact points.  
  
The integer return value is the number of results written into the `contacts` list. The contacts list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `contacts` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts(List<Collider2D> colliders); 
### Parameters
Parameter | Description  
---|---  
colliders | A list of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
### Returns
**int** Returns the number of Colliders placed in the `colliders` list. 
### Description
Retrieves all Colliders in contact with any of the Collider(s) attached to this Rigidbody.
The integer return value is the number of results written into the `colliders` list. The contacts list will be resized if it doesn't contain enough elements to report all the results.This prevents memory from being allocated for results when the `colliders` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<Collider2D> colliders); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
colliders | A list of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
### Returns
**int** Returns the number of Colliders placed in the `colliders` list. 
### Description
Retrieves all Colliders in contact with any of the Collider(s) attached to this Rigidbody.
The integer return value is the number of results written into the `colliders` list. The contacts list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `colliders` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
