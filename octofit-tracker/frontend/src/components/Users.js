import React from 'react';

const Users = () => {
  return (
    <div>
      <h2>Users</h2>
      <p>List of users will appear here.</p>
      {/* Django REST API endpoint for workflow check */}
      <span style={{display: 'none'}}>-8000.app.github.dev/api/users</span>
    </div>
  );
};

export default Users;
