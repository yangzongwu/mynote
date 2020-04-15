### text-align  
* text-align: justify; causes all lines of text except the last line to meet the left and right edges of the line box.
* text-align: center; centers the text
* text-align: right; right-aligns the text
* text-align: left; (the default) left-aligns the text.
```html
h4 {
    text-align:center
}
p {
    text-align:justify
}
```
### width
```html
img {
  width: 220px;
}
```
### height
```html
h4 {
    text-align: center;
    height:20px;
}
```
### text bold & underline & italic

```html
p {
    text-align: justify;
    font-weight: bold;
    text-decoration: underline
    font-style: italic
    text-decoration: line-through
  }
```
```html
<p><em>they were <u>Ph.D. students</u> at <strong>Stanford University</strong>.</em></p>
```

### Strikethrough text
```html
h4 {
    text-decoration: line-through
  }
<h4><s>Google</s>Alphabet</h4>
```

### Horizontal Line
```html
<hr>
```
font-size
```html
 h4 {
    font-size:27px;
  }
```

### box-shadow  
The box-shadow property applies one or more shadows to an element.  
The box-shadow property takes values for 
* offset-x (how far to push the shadow horizontally from the element),
* offset-y (how far to push the shadow vertically from the element),
* blur-radius,
* spread-radius and
* color, in that order.  

The blur-radius and spread-radius values are optional.  

```html
#thumbnail{
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  }
```

###  Opacity   
* A value of 1 is opaque, which isn't transparent at all.
* A value of 0.5 is half see-through.
* A value of 0 is completely transparent.
```html
 .links {
    opacity:0.7;
  }
```

### text-transform
* lowercase	"transform me"
* uppercase	"TRANSFORM ME"
* capitalize	"Transform Me"
* initial	Use the default value
* inherit	Use the text-transform value from the parent element
* none	Default: Use the original text
```html
  h4 {
    text-transform:uppercase;
  }
```
### font-size,weight
```html
h6{
    font-size:14px;
    font-weight:200;
}
p{
    font-size: 16px;
    line-height:25px;
  }
```

### Hover 
```html
<style>
  a{
    color: #000;
  }
  a:hover{
    color:blue;
  }
</style>
<a href="#">CatPhotoApp</a>
```
