```html
<form action="/url-where-you-want-to-submit-form-data"></form>
```
### text
```html
<input type="text">
<input type="text" placeholder="cat photo URL">
<input type="text" required>
```
### Submit Button
```html
<button type="submit">Click</button>
```
### Radio Button
```html
<label for="indoor">
    <input id="indoor" type="radio" name="indoor-outdoor">Indoor 
</label>
<label for="outdoor">
    <input id="outdoor" type="radio" name="indoor-outdoor"> Outdoor
</label>
```
### Checkboxes
```html
<form action="/submit-cat-photo">
    <label><input type="checkbox" name="personality"> Loving</label>
    <label><input type="checkbox" name="personality"> Lazy</label>
    <label><input type="checkbox" name="personality"> Energetic</label><br>
</form>
```
### value & checked
value:if do not have value when submit:indoor-outdoor==on else name==value
checked:default selected
```html
<form action="/submit-cat-photo">
    <label for="indoor"><input id="indoor" type="radio" name="indoor-outdoor" value="indoor" checked> Indoor</label>
    <label for="outdoor"><input id="outdoor" type="radio" name="indoor-outdoor" value="outdoor"> Outdoor</label><br>
    <label for="loving"><input id="loving" type="checkbox" name="personality" value="loving" checked> Loving</label>
    <label for="lazy"><input id="lazy" type="checkbox" name="personality" value="lazy"> Lazy</label>
    <label for="energetic"><input id="energetic" type="checkbox" name="personality" value="energetic"> Energetic</label><br>
    <input type="text" placeholder="cat photo URL" required>
    <button type="submit">Submit</button>
  </form>
```
# example
```html
<h1>Hotel Feedback Form</h1>
    <form method="get">
        <h2>Are your from inside the US or Outside the US</h2>
        <label for="inusa">Inside:</label>
        <input id="inusa" type="radio" name="loc" value="">
        <label for="outusa">Outusa:</label>
        <input id="outusa" type="radio" name="loc" value="">
        <h2>How was your service?</h2>
        <select name="stars">
            <option value="Greate">3</option>
            <option value="OKay">2</option>
            <option value="Bad">1</option>
        </select>
        <h2>Any other feedback?</h2>
        <textarea name="mytext" rows="8" cols="80"></textarea>
        <input type="submit" name="" value="SUBMIT">
    </form>
```

# example
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Couse</title>
</head>
<body>
    <h1>Course Sign Up Page</h1>
    <p>Please Node: First Name, Last Name, Password, and Email are required</p>
    <form>
        <label for="firstname">First Name</label>
        <input id="firstname" type="text" placeholder="First Name" required>
        <label for="lastname">Last Name</label>
        <input id="lastname" type="text" placeholder="Last Name" required>
        <br>
        <label for="email">Email</label>
        <input id="email" type="email" placeholder="name@email.com" required>
        <label for="password">Last Name</label>
        <input id="password" type="password" placeholder="Password" required>

        <p>Are you over the age of 18?</p>
        <label for="great18">Yes:</label>
        <input id="great18" type="radio" name="age">
        <label for="less18">No:</label>
        <input id="less18" type="radio" name="age">

        <p>Do you have a Credit Card or Paypal?</p>
        <select>
            <option value="Credit Card">Credit Card</option>
            <option value="Paypal">Paypal</option>
        </select>

        <input type="submit" value="Sign Up">
    </form>
</body>
</html>
```
