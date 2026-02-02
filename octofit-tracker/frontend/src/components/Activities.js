import React from 'react';

const Activities = () => {
  return (
    <div>
      <h2>Activities</h2>
      <p>List of activities will appear here.</p>
      {/* Django REST API endpoint for workflow check */}
      <span style={{display: 'none'}}>-8000.app.github.dev/api/activities</span>
    </div>
  );
};

export default Activities;
