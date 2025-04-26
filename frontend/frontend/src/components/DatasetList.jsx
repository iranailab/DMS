import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const DatasetList = () => {
  const [datasets, setDatasets] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/datasets/')
      .then((res) => res.json())
      .then((data) => setDatasets(data))
      .catch((err) => console.error('Error fetching datasets:', err));
  }, []);

  return (
    <div>
      <h2>Datasets</h2>
      <ul>
        {datasets.map((dataset) => (
          <li key={dataset.id}>
          <Link to={`/datasets/${dataset.id}`}>{dataset.title}</Link>
        </li>
        ))}
      </ul>
    </div>
  );
};

export default DatasetList;
