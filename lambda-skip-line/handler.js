'use strict';
console.log('Loading function');

exports.transform = (event, context, callback) => {
    const output = event.records.map((record) => ({
        recordId: record.recordId,
        result: 'Ok',
        data: record.data+"Cg==",
    }));
    console.log(`Processing completed.  Successful records ${output.length}.`);
    callback(null, { records: output });
};