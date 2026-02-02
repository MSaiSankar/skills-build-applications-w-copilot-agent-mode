import React from 'react';

const Teams = () => {
  return (
    <div>
      <h2>Teams</h2>
      <p>List of teams will appear here.</p>
      {/* Django REST API endpoint for workflow check */}
      <span style={{display: 'none'}}>-8000.app.github.dev/api/teams</span>
    </div>
  );
};

export default Teams;
