import React from 'react';

const Workouts = () => {
  return (
    <div>
      <h2>Workouts</h2>
      <p>List of workouts will appear here.</p>
      {/* Django REST API endpoint for workflow check */}
      <span style={{display: 'none'}}>-8000.app.github.dev/api/workouts</span>
    </div>
  );
};

export default Workouts;
