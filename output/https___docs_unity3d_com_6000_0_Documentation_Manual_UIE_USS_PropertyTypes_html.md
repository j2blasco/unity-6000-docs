* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-PropertyTypes.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Style UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [USS properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-properties.html)
  * USS data types


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-properties.html)
USS properties
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-SupportedProperties.html)
USS common properties
# USS data types
USS data types define typical values, including keywords and units, that USS properties and functions accept. 
## Syntax
USS properties use the same syntax as W3C CSS documents:
  * Keyword values appear as is. For example: `auto`, `baseline`.
  * Basic data types appear between angle brackets ( `<` and `>`). For example: `<length>` and `<color>`.
  * Non-terminals that share the same name as a property appear between angle brackets and single straight quotes ( `<'` and `'>`). For example, `<'width'>`.


If a property value has more than one option, the following applies:
  * Side-by-side words mean that all options must occur in the given order.
  * A bar (`|`) separates two or more options. One of them must occur.
  * Double bars (`||`) separate two or more options. One or more of them must occur in any order.
  * Double ampersands (`&&`) separate two or more options. All options must occur.
  * Square brackets (`[` `]`) denote grouping.


Every type, keyword, or angle-bracketed group might be followed by modifiers. The following table lists the possible modifiers:
**Modifier** | **The preceding type, keyword, or group**  
---|---  
An asterisk (`*`) | Occurs zero or more times  
A plus sign (`+`) | Occurs one or more times  
A question mark (`?`) | Is optional  
A pair of numbers in curly braces (`{A,B}`) | Occurs at least `A` and at most `B` times  
## Length
UI Toolkit supports  pixels(`px`) and percentages (`%`) as units of measurement for length. Pixel values are absolute, while percentages are relative to the element’s parent.
Examples:
  * `width:200px;` expresses a width of 200 px.
  * `width:50%;` expresses a width of half of the parent element’s width.


It’s important to specify the unit of measurement. If you don’t specify a unit of measurement, UI Toolkit assumes that the property value is expressed in px.
**Note:** `0` is a special value that doesn’t require a unit of measurement.
## Numeric
Numeric values are expressed as either floating points or integer literals. For example, `flex:1.0`.
## Keywords
Specific keywords are supported for some built-in properties. Keywords give a descriptive name instead of a number. For example: `position:absolute`. 
All properties support the `initial` global keyword which resets the default value of a property to an element. 
In the following example, although you set the color of all the labels to red, the `initial` keyword of `color` restores the color of `label1` to its default value:
```
/* Set the color of all the labels to red. */
Label {
    color: red;
}
/* label1 is the name of a specific label. */
#label1{
    color: initial;
}

```

## Color
UI Toolkit supports the following literal color values and functions:
  * A Hexadecimal value: `#FFFF00`, `#0F0`
  * The RGB function: `rgb(255, 255, 0)`
  * The RGBA function: `rgba(255, 255, 0, 1.0)`
  * [Color keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-color-keywords.html)


## Assets
You can reference project assets such as fonts and textures from your USS files. For example, you might reference a texture to use as the background image for an element.
To reference an asset, you can use either the `url()` function or the `resource()` function: 
  * `resource()`: Represents an asset in a `Resources` folder.
  * `url()`: Represents an asset specified by a path. You can express it as either a relative path or an absolute path.


Use the `url()` function in most cases. However, the `resource()` function supports automatically loading different versions of image assets for different screen densities.
### Reference assets with the URL function
When you reference an asset with the `url()` function, the path you specify can be relative or absolute:
  * Relative paths must be relative to the folder that contains the USS file that references the asset.
  * Absolute paths are relative to the project.


The path must include the file extension.
For example, if your project has a `USS` folder that contains all your style sheets, and a `Resources` folder that contains all your image assets.
```
Assets
  └─ Editor
      └─ Resources
      └─ USS

```

To reference an image named `thumb.png`, you can use one of the following paths:
Relative path | Absolute path  
---|---  
`url("../Resources/thumb.png")` |  `url("/Assets/Editor/Resources/thumb.png")`  
  
`url("project:/Assets/Editor/Resources/thumb.png")`   
  
`url("project:///Assets/Editor/Resources/thumb.png")`  
To reference an image in a package, use the `Packages` folder in the path:
Relative path | Absolute path  
---|---  
`url("../Packages/com.my.example.package/Editor/Resources/thumb.png")` | `url("Project:///Packages/com.my.example.package/Editor/Resources/thumb.png")`  
### Reference assets with the resource function
The `resource()` function can reference assets in Unity’s resource folders (`Resources` and `Editor Default Resources`). You reference an asset by name.
  * If the file is in the `Editor Default Resources` folder, you must include the file extension.
  * If the file is in the `Resources` folder, you must not include the file extension.


For example:
Path to file | Reference syntax  
---|---  
`Assets/Resources/Images/my-image.png` | `resource("Images/my-image")`  
`Assets/Editor Default Resources/Images/my-image.png` | `resource("Images/default-image.png")`  
### Reference image assets for High DPI/Retina screens
To support screens with different screen densities (DPI), do the following:
  * Make sure that the high DPI versions of your textures have a `@2x` suffix in their file names. For example the high DPI version of `myimage.png` should be `myimage@2x.png`
  * Place the regular and high DPI versions of the texture assets in the same project folder.


When Unity loads the asset, it automatically chooses the correct version for the current screen DPI.
For example, if you use `resource("myimage")` in USS, Unity loads either `Resources/myimage.png` or `Resources/myimage@2x.png`.
## Strings
Use quotes to specify a string value. For example: `--my-property: "foo"`.
## Additional resources
  * [USS color keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Properties-Reference.html)
  * [USS common properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-SupportedProperties.html)
  * [USS properties reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Properties-Reference.html)
  * [USS custom properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-CustomProperties.html).
  * [Style UI with UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-using-uss-selectors.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-properties.html)
USS properties
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-SupportedProperties.html)
USS common properties
