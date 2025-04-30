import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ResourceCreateForm = () => {
  const { id: datasetId } = useParams();
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    file: null,
  });

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: files ? files[0] : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const data = new FormData();
    data.append('name', formData.name);
    data.append('description', formData.description);
    data.append('file', formData.file);
    data.append('dataset', datasetId);  // خیلی مهمه!

    axios.post('/api/resources/', data, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      withCredentials: true,
    }).then(() => {
      alert('ریسورس با موفقیت اضافه شد');
    }).catch(err => {
      console.error(err);
      alert('خطا در افزودن ریسورس');
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>افزودن ریسورس برای دیتاست {datasetId}</h2>

      <label>نام فایل:</label>
      <input type="text" name="name" onChange={handleChange} required />

      <label>توضیحات:</label>
      <textarea name="description" onChange={handleChange} />

      <label>فایل:</label>
      <input type="file" name="file" onChange={handleChange} required />

      <button type="submit">افزودن ریسورس</button>
    </form>
  );
};

export default ResourceCreateForm;
