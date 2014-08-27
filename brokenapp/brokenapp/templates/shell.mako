<h1>Shell Injection</h1>
<p>Give the file you wish to cat</p>
<p>List of files:</p>
<p>${c.out}</p>
<form name="test" method="post" action="/shellinjection/inject">
Filename: <input type="text" name="filename" />
<input type="submit" name="submit" value="Submit" />
</form>
