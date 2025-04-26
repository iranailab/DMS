import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const DatasetDetail = () => {
  const { id } = useParams();
  const [dataset, setDataset] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/api/datasets/${id}/`)
      .then(res => res.json())
      .then(data => setDataset(data))
      .catch(err => console.error(err));
  }, [id]);

  if (!dataset) return <p>Loading...</p>;

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-2">{dataset.title}</h2>
      <p className="text-gray-600 mb-4">{dataset.description}</p>

      <div className="mb-4">
        <strong>Organization:</strong>{' '}
        {dataset.organization ? dataset.organization.name : 'None'}
      </div>

      <div className="mb-4">
        <strong>License:</strong>{' '}
        {dataset.license ? dataset.license.title : 'None'}
      </div>

      <div className="mb-4">
        <strong>Tags:</strong>{' '}
        {dataset.tags && dataset.tags.length > 0
          ? dataset.tags.map((tag) => tag.name).join(', ')
          : 'None'}
      </div>

      <div className="mb-4">
        <strong>Categories:</strong>{' '}
        {dataset.categories && dataset.categories.length > 0
          ? dataset.categories.map((cat) => cat.name).join(', ')
          : 'None'}
      </div>

      <div className="mb-4">
        <strong>Created at:</strong> {new Date(dataset.created).toLocaleDateString()}
      </div>

      <h3 className="text-xl font-semibold mt-6 mb-2">Resources</h3>
      {dataset.resources && dataset.resources.length > 0 ? (
        <ul className="list-disc pl-6">
          {dataset.resources.map((res) => (
            <li key={res.id}>
              <a href={res.file || res.url} className="text-blue-600 underline" target="_blank" rel="noopener noreferrer" download>
                {res.name || res.file || res.url}
              </a>
            </li>
          ))}
        </ul>
      ) : (
        <p>No resources available.</p>
      )}
    </div>
  );
}

export default DatasetDetail;
