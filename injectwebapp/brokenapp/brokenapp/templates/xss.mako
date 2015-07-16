<h1>XSS</h1>
<p>Do evil things</p>
<form name="test" method="post" action="/xss/inject">
Payload: <input type="text" name="data" />
<input type="submit" name="submit" value="Submit" />
</form>
Click <a href="/xss/inject?data=<script>alert(document.cookie)</script>">here</a> for more evil!
