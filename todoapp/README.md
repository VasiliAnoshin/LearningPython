<h1 id="flask-migrate">Flask-Migrate</h1>
<p>We want to allow the user to check or uncheck todo items in our Todo app, to mark them as completed or not. Right now, we don't have a concept of what "completed" means in our database, which models a Todo with a single property called "description". We'd like to extend the model to also include a boolean property called "completed" in order to allow for todos to be marked as completed or not by a user on our app.</p>

<p>While we can do this totally using <code>psql</code> or another Postgres client to simply alter our table to add a new column using the <code>ALTER TABLE ADD COLUMN</code> command in SQL, we should use <strong>migrations</strong> to handle changes to our database schema for better maintainability and the ability to rollback quickly in case of issues.</p>

<div class="index-module--markdown--2MdcR ureact-markdown "><p>Have the documentation available as you work. Links:</p>
    <ul>
    <li><a target="_blank" href="https://flask-migrate.readthedocs.io/en/latest/">Flask-Migrate documentation</a></li>
    <li><a target="_blank" href="https://alembic.sqlalchemy.org/en/latest/">Alembic documentation</a></li>
    </ul>
    <p>Next, install Flask-Migrate by running:</p>
    <pre><code class="lang-bash">pip3 install Flask-Migrate
    </code></pre>
</div>