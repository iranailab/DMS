import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const DatasetCreateForm = () => {
    const [formData, setFormData] = useState({
      name: '',
      description: '',
      version: '',
      license: '',
      organization: '',
      private: false,
    });
  
    const [availableOrganizations, setAvailableOrganizations] = useState([]);
    const [licenses, setLicenses] = useState([]);
  
    const navigate = useNavigate();

    useEffect(() => {
      // گرفتن لیست سازمان‌هایی که کاربر عضو آن‌هاست
      axios.get('/api/datasets/')
        .then(res => {
          if (res.data.length > 0 && res.data[0].available_organizations) {
            setAvailableOrganizations(res.data[0].available_organizations);
          }
        });
  
      // گرفتن لیست مجوزها
      axios.get('/api/licenses/')
        .then(res => {
            console.log('licenses response:', res.data);
          setLicenses(res.data);
        });
    }, []);
  
    const handleChange = (e) => {
      const { name, value, type, checked } = e.target;
      setFormData(prev => ({
        ...prev,
        [name]: type === 'checkbox' ? checked : value
      }));
    };
  
    const handleSubmit = (e) => {
      e.preventDefault();
      axios.post('/api/datasets/', formData, {
        headers: {
          'Content-Type': 'application/json'
        },
        withCredentials: true // برای کوکی و لاگین
      }).then(res => {
        alert('دیتاست با موفقیت اضافه شد');
        setFormData({
          name: '',
          description: '',
          version: '',
          license: '',
          organization: '',
          private: false,
        });
        const datasetId = res.data.id;

        // انتقال به صفحه اضافه کردن ریسورس
        navigate(`/datasets/${datasetId}/resources/add`);
      }).catch(err => {
  if (err.response) {
    console.error('Server responded with:', err.response.data);
    alert('خطا در افزودن دیتاست: ' + JSON.stringify(err.response.data));
  } else if (err.request) {
    console.error('No response received:', err.request);
    alert('خطا در اتصال به سرور');
  } else {
    console.error('Error setting up request:', err.message);
    alert('خطا در تنظیم درخواست');
  }
});
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <h2>افزودن دیتاست جدید</h2>
  
        <label>نام:</label>
        <input type="text" name="name" value={formData.name} onChange={handleChange} required />
  
        <label>توضیحات:</label>
        <textarea name="description" value={formData.description} onChange={handleChange} />
  
        <label>نسخه:</label>
        <input type="text" name="version" value={formData.version} onChange={handleChange} />
  
        <label>مجوز:</label>
        <select name="license" value={formData.license} onChange={handleChange}>
          <option value="">انتخاب مجوز</option>
          {licenses.map(lic => (
            <option key={lic.id} value={lic.id}>{lic.title}</option>
          ))}
        </select>
  
        <label>سازمان:</label>
        <select name="organization" value={formData.organization} onChange={handleChange}>
          <option value="">انتخاب سازمان</option>
          {availableOrganizations.map(org => (
            <option key={org.id} value={org.id}>{org.name}</option>
          ))}
        </select>
  
        <label>
          <input type="checkbox" name="private" checked={formData.private} onChange={handleChange} />
          خصوصی باشد؟
        </label>
  
        <button type="submit">افزودن</button>
      </form>
    );
  };
  
  export default DatasetCreateForm;